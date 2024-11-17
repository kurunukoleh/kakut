from flask import *
from datamanager import DBMmanager

app = Flask("kakut")
db_name = "Kakut.db"
@app.route("/")
def index():
    db_manager = DBMmanager(db_name)
    quizess = db_manager.get_quises()
    return render_template("index.html" , quizess = quizess)

@app.route("/svaz")
def svaz():
    return render_template("sviaz.html")

app.run()