from flask import url_for, Blueprint, render_template, redirect, session, flash, request
import utils

add = Blueprint(__name__, "add")

@add.route("/add/", methods=['GET', 'POST'])
def func():
    if "login" not in session:
        return redirect("/login/")
    if request.method == "POST":
        name = request.form['name']
        date = request.form['date']
        budget = request.form['budget']
        features = request.form['features'].replace("\r", '').split("\n")
        if not utils.db.projects.find_one({"username":session['login'], "name":name, "completed":False}):
            utils.db.projects.insert({"username":session['login'], "name":name, "deadline":date, "price":budget, "features":features, "completed":False, "features_completed":[], "messages":[], "amount_of_features":len(features)})
            
            return redirect("/dashboard/")
        else:
            flash("You already used that name.")
    return render_template("add.html")
