from flask_sqlalchemy import SQLAlchemy
from faker import Faker
from datetime import datetime, timezone
from models import db, Restaurant, Pizza, Restaurant_pizza
from app import app

fake = Faker()
app.app_context().push()

# Function to create fake data and add to the database
def seed_data():
    # Clear existing data
    db.session.query(Restaurant_pizza).delete()
    db.session.query(Restaurant).delete()
    db.session.query(Pizza).delete()
    db.session.commit()
 # Create Restaurants
    restaurant1 = Restaurant(name='Restaurant A', address='123 Main St')
    restaurant2 = Restaurant(name='Restaurant B', address='456 Oak St')

    # Create Pizzas
    pizza1 = Pizza(name='Margherita', ingredients='Tomato, Mozzarella, Basil')
    pizza2 = Pizza(name='Pepperoni', ingredients='Pepperoni, Cheese, Tomato Sauce')

    # Add Restaurants and Pizzas to the session
    db.session.add_all([restaurant1, restaurant2, pizza1, pizza2])
    db.session.commit()

    # Create Restaurant_pizzas (Associations)
    association1 = Restaurant_pizza(restaurant=restaurant1, pizza=pizza1, price=10)
    association2 = Restaurant_pizza(restaurant=restaurant1, pizza=pizza2, price=12)
    association3 = Restaurant_pizza(restaurant=restaurant2, pizza=pizza1, price=11)

    # Add Restaurant_pizzas to the session
    db.session.add_all([association1, association2, association3])
    db.session.commit()

if __name__ == '__main__':
    seed_data()