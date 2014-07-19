from flask import Blueprint, render_template, redirect, session, flash, request

dashboard = Blueprint(__name__, "dashboard")

@dashboard.route("/dashboard/", methods=['GET', 'POST'])
def func():
    if "login" not in session:
        return redirect("/login/")
    if request.method == "POST":
        pass
    
    project = utils.db.project.find({"username":session['login']})
    
    return render_template("dashboard.html", data=data)
