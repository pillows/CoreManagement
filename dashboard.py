from flask import Blueprint, render_template, redirect, session, flash, request
import utils

dashboard = Blueprint(__name__, "dashboard")

@dashboard.route("/dashboard/", methods=['GET', 'POST'])
def func():
    if "login" not in session:
        return redirect("/login/")
    if request.method == "POST":
        pass
    
    projects = utils.db.projects.find({"username":session['login'], "completed":False})

    return render_template("dashboard.html", projects=projects)
