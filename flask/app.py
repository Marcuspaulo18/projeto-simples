from flask import Flask,render_template

app = Flask(__name__,template_folder="pagina")

@app.route("/inicio")
@app.route("/")
def hom():
    return render_template("suino.html")

if __name__ == "__main__":
    app.run(debug=True)
