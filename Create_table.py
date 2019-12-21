##import mysql package
import mysql.connector
#connect to local machine
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  #user="datarep",  # this is the user name on my mac
  #passwd="password" # for my mac
  database="twitter2"
)

cursor = db.cursor()
#create table followers2 with id as primary key and one field: 'name'
sql="CREATE TABLE Followers2 (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(255))"

cursor.execute(sql)

