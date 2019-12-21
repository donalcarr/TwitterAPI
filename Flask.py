#use flask create a web server on your local machine
from flask import Flask, jsonify
#import twitterDAO class
from followersDAO import twitterDAO

#creates app that hosts application
app = Flask(__name__, static_url_path='', static_folder='.')

#curl "http://127.0.0.1:5000/twitter2
#route that calls a function
@app.route('/twitter2')

def getAll():
    results = twitterDAO.getAll()
    #return results to the web browser
    return jsonify(results)
    
@app.route('/twitter2/<int:id>' , methods=['DELETE'])
def delete(id):
    twitterDAO.delete(id)
    #return "done" to the web browser after record is deleted
    return jsonify({"done":True})


if __name__ == '__main__' :
    app.run(debug= True)