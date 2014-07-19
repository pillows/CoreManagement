from flask import request, Blueprint, render_template, redirect, session, flash
from bson import ObjectId
import utils
import time
from timeago import timeago 

project = Blueprint(__name__, "project")

@project.route("/project/<_id>", methods=['GET', 'POST'])
def func(_id):
    db = utils.db
    if request.method == "POST":
        if request.form.get("feature"):
            feature = request.form['feature'].replace("\r", '').replace("\n", '')
            db.projects.update({"_id":ObjectId(_id)}, {"$push":{"features_completed":feature}})
            db.projects.update({"_id":ObjectId(_id)}, {"$pull":{"features":feature}})
            return redirect("/project/"+_id)
        if request.form.get("message"):
            message = request.form['message']
            message = {"message":message, "time":time.time()}
            db.projects.update({"_id":ObjectId(_id)}, {"$push":{"messages":message}})
    project = db.projects.find_one({"_id":ObjectId(_id)})
    project['messages'] = sorted(project['messages'], key = lambda x: x['time'])
    project['messages'].reverse()
    messages = []
    for x in project['messages']:
        t = timeago(time.time() - x['time'])
        x['timeago'] = str(int(t['value'])) + " " +t['type']
        messages.append(x)
    return render_template("project.html", job=project, messages=messages)
