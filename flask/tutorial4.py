from flask import Flask,redirect,url_for ,render_template, request

app = Flask(__name__, template_folder="template")

@app.route("/starting/")
def inicio():
    return render_template("novo.html")

@app.route("/login",methods=["POST","GET"])
def login():
    if request.method =="POST":
        user = request.form["nm"]
        return redirect(url_for("user",usr=user))
    else:
        return render_template("login.html")

@app.route("/user")
def user():
    return f"<h1></h1>"


if __name__ == "__main__":
    app.run(debug=True)
