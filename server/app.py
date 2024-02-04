from flask import Flask, jsonify, request, make_response
from flask_migrate import Migrate
from flask_restful import Api, Resource

from models import db,Restaurant

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///Restaurant.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

migrate=Migrate(app,db)
db.init_app(app)
api = Api(app)

class Restaurants(Resource):
    def get (self):
        restaurant=[ {"id":restaurant.id,"name":restaurant.name,"address":restaurant.address}for restaurant in Restaurant.query.all()]   
        return make_response(jsonify(restaurant),200) 


api.add_resource(Restaurants,'/restaurants')    


if __name__ == '__main__':
    app.run(port=5555,debug=True)
