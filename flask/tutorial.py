from flask import Flask,redirect,url_for,render_template

app = Flask(__name__,template_folder="templates")

@app.route("/")
def home():
    return"<h1>Hello world</h1>"

@app.route("/seco")
def second():
    return"<h2>this is a second page,let it balling</h2>"
@app.route("/terc")
def third():
    return render_template("olamundo.html")
@app.route("/<name>")
def user(name):
    return f"ola {name}"
if __name__=="__main__":
    app.run()