import mysql.connector
#create Twitter DAO class that stores functions
class TwitterDAO:
    db=""
    #mysql connection function
    def __init__(self): 
        self.db = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="twitter2"
        )
    
    #retrieve all followers from followers2 table
    def getAll(self):
        cursor = self.db.cursor()
        sql="select * from followers2"
        cursor.execute(sql)
        results = cursor.fetchall()
        ##return results
        returnArray = []
        print(results)
        for result in results:
            print(result)
            returnArray.append(self.convertToDictionary(result))
        ##return instead
        print (returnArray)

    #delete record based on id inputted to web page
    def delete(self, id):
        cursor = self.db.cursor()
        sql="delete from followers2 where id = %s"
        values = (id,)

        cursor.execute(sql, values)

        self.db.commit()
        print("delete done")
    
    #convert results retrieved to dictionery
    def convertToDictionary(self, results):
        colnames=['name']
        item = {}
        
        if results:
            for i, colName in enumerate(colnames):
                value = results[i]
                item[colName] = value
        
        return item

#create class
twitterDAO = TwitterDAO()