from flask import Flask, session, redirect
from project import project
from register import register
from login import login
from settings import settings
from dashboard import dashboard

app = Flask(__name__)
app.secret_key = "ASD'l1l;23k123kk;laskd;askd;lakSD;;alsmmzxcmmadf;kas;DK;lkl;1;23k1;23k;SAd00123lal;sdk;SAKD;lk213123"
app.debug = True
port = 5000

app.register_blueprint(dashboard)
app.register_blueprint(login)
app.register_blueprint(register)
app.register_blueprint(settings)
app.register_blueprint(project)

@app.route("/")
def index():
    if "login" not in session:
        return redirect("/login/")
    else:
        return redirect("/dashboard/")



if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=port)
