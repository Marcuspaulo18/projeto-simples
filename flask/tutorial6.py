from flask import Flask,redirect,url_for ,render_template, request,session,flash
from datetime import timedelta

app = Flask(__name__, template_folder="template")
app.secret_key="hello"
app.permanent_session_lifetime = timedelta(minutes=5)
@app.route("/starting/")
def inicio():
    return render_template("novo.html")

@app.route("/login",methods=["POST","GET"])
def login():
    flash("login sucessful!")
    if request.method =="POST":
        session.permanent=True
        user = request.form["nm"]
        session["user"]=user
        return redirect(url_for("user",usr=user))
    else:
        flash("logged in sucessful!")
        if "user" in session:
            return redirect(url_for("user"))

        return render_template("login.html")

@app.route("/user")
def user():
    if "user" in session:
     user=session["user"]
     return render_template("user.html",user=user)
    else:
        return redirect(url_for("login"))
@app.route("/logout")
def logout():
    session.pop("user",None)
    flash("você saiu,{user},info")
    return redirect(url_for("login"))

if __name__ == "__main__":
    app.run(debug=True)