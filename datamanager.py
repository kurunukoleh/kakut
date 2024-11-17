import sqlite3
class DBMmanager:
    def __init__(self , db_name):
        self.connection = sqlite3.connect(db_name)

    def create_tables(self):
        cursor = self.connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Quis(
                id INT PRIMARY KEY,
                title VARCHAR(255),
                description TEXT
            );
        
        """)

        cursor.execute("""
          CREATE TABLE IF NOT EXISTS Questions(
            question_id INT PRIMARY KEY,
            quiz_id INT,
            content TEXT
          );
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS Options(
                option_id INT PRIMARY KEY,
                question_id INT,
                content TEXT,
                Is_correct BOOlEAN
            );
        """)

        self.connection.commit()

    def addd_quiz(self , id , title , description):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Quis(id , title, description) VALUES (? , ? , ?) ", [id , title , description])
        self.connection.commit()
        cursor.close()

    def addd_option(self , option_id , question_id , content , Is_correct):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Options(option_id , question_id, content ,Is_correct ) VALUES (? , ? , ?) ", [option_id , question_id , content , Is_correct])
        self.connection.commit()
        cursor.close()

    def addd_question(self , question_id , quiz_id , content):
        cursor = self.connection.cursor()
        cursor.execute("INSERT INTO Questions(question_id , quiz_id, content) VALUES (? , ? , ?) ", [question_id , quiz_id , content])
        self.connection.commit()
        cursor.close()

    def get_quises(self):
        cursor = self.connection.cursor()

        cursor.execute("SELECT * FROM Quis")
        res = cursor.fetchall()
        cursor.close()
        return res

    def get_question(self , quiz_id):
        cursor = self.connection.cursor()
        cursor.execute("SELECT * FROM Questions WHERE quiz_id = ?" , [quiz_id])
        res = cursor.fetchall()
        cursor.close()
        return res