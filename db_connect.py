import mysql.connector as my
def myself():
    return my.connect(
        host="localhost",
        user="root",
        password="",
        database="manage_db"
        )
