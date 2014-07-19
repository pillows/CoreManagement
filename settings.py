from flask import Blueprint, render_template, redirect, session, flash
import utils

settings = Blueprint(__name__, "settings")

@settings.route("/settings/", methods=['GET', 'POST'])
def func():
    pass
