from flask import Flask, render_template

app = Flask(__name__, template_folder="template")

@app.route("/starting/")
def inicio():
    return render_template("novo.html",content="Testing12334")

if __name__ == "__main__":
    app.run(debug=True)
