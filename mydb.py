import mysql.connector

dataBase = mysql.connector.connect(
    host = "localhost",
    user = "root",
    passwd = "Bautista.06fam",
)

#preare a cursor object
cursorObject = dataBase.cursor()

#create a database
cursorObject.execute("CREATE DATABASE db_dcrm")

print("Database has been created")