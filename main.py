from datamanager import DBMmanager

db_manager = DBMmanager("kakut.db")
db_manager.create_tables()

#db_manager.addd_quiz(4 , "квіз про нігерйв йоу" , "еукуайцсцс")
#print(db_manager.get_quises())
#db_manager.addd_question(1 , 2 , "fvaagrgr")
db_manager.get_question(2)