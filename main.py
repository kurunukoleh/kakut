from datamanager import DBMmanager

db_manager = DBMmanager("kakut.db")
db_manager.create_tables()

#print(db_manager.get_quises())
#db_manager.addd_quiz(6 , "квіз по гимну" , "хо ниравилно ивдповисть на вси  питання той хадер")
#db_manager.addd_question(15 , 6 , "ха відповиси а це питтаана правилно і получи гимна кусок")
db_manager.get_question(2)