from flask import Blueprint, render_template, redirect, session, flash, request
import utils

register = Blueprint(__name__, "register")

@register.route("/register/", methods=['GET', 'POST'])
def func():
    if "login" in session:
        return redrect("/")
    
    if request.method == "POST":
        email = request.form['email']
        username = request.form['username'].lower()
        password = utils.protect(request.form['password'])
        if not utils.db.members.find_one({"username":username}):
            utils.db.members.insert({"username":username, "password":password, "email":email})
            session['login'] = username
            return redirect("/")
        else:
            flash("Username taken")
            return redirect("/register/")

    return render_template("register.html")
