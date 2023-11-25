from flask import Flask, render_template, request, session, redirect
from flask_session import Session

app = Flask(__name__)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

@app.route("/")
def HomeFun():
    if not session.get("username"):
        return redirect("/login")
    return render_template("home.html")

@app.route("/login", methods=['POST', 'GET'])
def LoginFun():
    if request.method=="POST":
        session["username"]=request.form.get("username")
        return redirect("/")
    return render_template("login.html")

@app.route("/logout")
def LogoutFun():
    session['username']=None
    return redirect("/")

if __name__=="__main__":
    app.run(debug=True)