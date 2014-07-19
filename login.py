from flask import Blueprint, render_template, redirect, session, flash, request
import utils

login = Blueprint(__name__, "login")

@login.route("/login/", methods=['GET', 'POST'])
def func():
    if "login" in session:
        return redirect("/")
    if request.method == "POST":
        username = request.form['username'].lower()
        password = utils.protect(request.form['password'])
        if utils.db.members.find_one({"username":username, "password":password}):
            session['login'] = username
            return redirect("/")
        else:
            flash("Login Failed")
            return redirect("/login/")

    return render_template("login.html")
