from flask import *

app = Flask("kakut")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/svaz")
def svaz():
    return render_template("sviaz.html")

app.run()