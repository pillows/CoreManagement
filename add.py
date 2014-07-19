from flask import Blueprint, render_template, redirect, session, flash, request
import utils

add = Blueprint(__name__, "add")

@add.route("/add/", methods=['GET', 'POST'])
def project_add():
    return render_template("add.html")