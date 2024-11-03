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