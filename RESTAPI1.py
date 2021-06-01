#RESTAPIs with Flask  & Python
from flask import Flask, json, jsonify

app = Flask(__name__)

stores = [
    {
        'name' : 'Twills',
        'items' : [
            {
                'name' : 'jeans',
                'price' : 1600
            }

        ]

        
    }
]
#Post __ Used to receive a data

#GET __ Used to send data back only



#Post/store data: {name :}
@app.route('/store', methods = ['POST'])
def create_store():
    pass


#Get/store/<string : name>
@app.route('/store/<string:name>')
def get_store(name):
    pass 


#Get/store
@app.route('/store')
def get_stores():
    return jsonify({'stores' : stores})

#Post/store/<string: name>/item
@app.route('/store/<string:name>/item', methods = ['POST'])
def create_item_in_store(name):
    pass
#Get/store/<string: name>/item
@app.route('/store/<string:name>/item')
def get_item_in_store(name):
    pass 


app.run(port=5000)

#Finally run it in terminal and then we get http link
#we have to copy that link and post it in chrome like "http//..../store"
#now we get solution.