from flask import *
from datamanager import DBMmanager

app = Flask("kakut")
db_name = "Kakut.db"
app.secret_key = "1488"

@app.route("/")
def index():
    db_manager = DBMmanager(db_name)
    quizess = db_manager.get_quises()
    return render_template("index.html" , quizess = quizess)

@app.route("/svaz")
def svaz():
    return render_template("sviaz.html")

@app.route("/quizz/<int:quizz_id>")
def get_question(quizz_id):
    db_manager = DBMmanager(db_name)
    questions = db_manager.get_question(quizz_id)
    session["questions"] = questions
    session["true_ans"] = 0
    session["quest_index"] = 0

    return redirect(url_for("show_question" , quizz_id=quizz_id))

@app.route("/quizz/<int:quizz_id>/question")
def show_question(quizz_id):
    nomer = session["quest_index"]
    q = session["questions"][nomer]
    db_manager = DBMmanager(db_name)
    options = db_manager.get_options(q[0])

    return render_template("question.html" , question=q , options=options , quizz_id=quizz_id)

@app.route("/quizz/<int:quizz_id>/answer" , methods=["POST" , "GET"])
def answer_func(quizz_id):
    session["quest_index"]+=1
    selected_value = request.form.get('answer')

    if len(session["questions"]) <= session["quest_index"]:
        return redirect(url_for("result" , quizz_id=quizz_id ))
    else:
        if selected_value == "1":
            session["true_ans"] += 1
            print(selected_value)
        return redirect(url_for("show_question" , quizz_id=quizz_id))




@app.route("/quizz/<int:quizz_id>/result")
def result(quizz_id):
    return render_template("answers.html")

app.run()