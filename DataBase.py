import sqlite3

def createTable():
    connection= sqlite3.connect("LoginICU.db")

    connection.execute("CREATE TABLE USERS(USERNAME TEXT NOT NULL ,PASSWORD TEXT)")
    connection.execute("Insert into users values(?,?,?)",('Marinajata','090596','111'))
    connection.commit()
    result=connection.execute("Select * from users ")
    for data in result:
        print("Username :" ,data[0])
        print("Password :" ,data[1])
        print("Usercode :" ,data[2])

    connection.close()
createTable()    
