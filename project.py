from flask import Blueprint, render_template, redirect, session, flash
from bson import ObjectId
import utils

project = Blueprint(__name__, "project")

@project.route("/project/<_id>")
def func(_id):
    db = utils.db
    project = db.projects.find_one({"_id":ObjectId(_id)})
    return render_template("project.html", project=project)
