##import mysql package
import mysql.connector
#connect to local machine
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password=""
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
)

cursor = db.cursor()
#create database twitter2
cursor.execute("CREATE DATABASE Twitter2")
