from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy import MetaData
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

metadata = MetaData(naming_convention={
    "fk": "fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s",
})

db = SQLAlchemy(metadata=metadata)

    
    


class Restaurant(db.Model, SerializerMixin):
    __tablename__ = 'restaurant'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    address = db.Column(db.String)
    
    pizzas = db.relationship("Pizza", secondary="restaurantpizzas", backref="restaurant")
    restaurant_pizza = db.relationship("Restaurant_pizza", backref="restaurant")


class Pizza(db.Model, SerializerMixin):
    __tablename__ = 'pizza'
  
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    ingredients = db.Column(db.String)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
  
    restaurant_pizza = db.relationship("Restaurant_pizza", backref="pizza")

class Restaurant_pizza(db.Model, SerializerMixin):
    __tablename__ = 'restaurantpizzas'
  
    id = db.Column(db.Integer, primary_key=True)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'))
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'))
    price = db.Column(db.Integer)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
@validates("price")
def validates_price(self,key,price):
    if not 1<= price <=30:
        raise ValueError("price must be between 1 and 30")
    return price