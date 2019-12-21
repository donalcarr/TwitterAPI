import mysql.connector
#https://python-twitter.readthedocs.io/en/latest/getting_started.html
#package used for retrieving data from Twitter API
import twitter
#import pandas package for analysing twitter data
import pandas as pd

#connect to API using personal keys for my twitter account
api = twitter.Api(consumer_key='eVgG3aXSDrcC8qsDYCpRuEL5b',
  consumer_secret='xGu7CXK96zXL9FlCPXskRoK66upzoQhEugIm8YSonx0K1eOLop',
    access_token_key='3786592272-f794mw0GDYWXzsWRcEZq66h6kMNDjiUoA83whE2',
    access_token_secret='p3OaezhYgNiM7vyfC3PqHQWtQTjocOhLZjQtsxMZR77dw')

#after connection extract 20 persons I follow
followers2 = api.GetFriends(total_count=20)


#print each follower to console
for follower in followers2:
    print(follower.name)

#create a list
item = [] 
#append each follower to the list
for follower in followers2:
    item.append(follower.name)

##print(item)




#connect to mysql twitter2 database
db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="twitter2"
)

#create a dataframe for item
df = pd.DataFrame(item)
#convert to list
val_to_insert = df.values.tolist()
#create cursor object 
cursor = db.cursor()
#sql to insert data into followers2 table
sql="INSERT into followers2 (name) VALUES (%s)"
#insert list
cursor.executemany(sql, val_to_insert)

db.commit()
print("records inserted, ID:", cursor.lastrowid)