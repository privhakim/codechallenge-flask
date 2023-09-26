from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Restaurant(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True, nullable=False)
    address = db.Column(db.String(255), nullable=False)
    pizzas = db.relationship(
        'Pizza',
        secondary='restaurant_pizza',
        back_populates='restaurants',
        overlaps="restaurant_pizzas"
    )

class Pizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    ingredients = db.Column(db.String(255), nullable=False)
    restaurants = db.relationship(
        'Restaurant',
        secondary='restaurant_pizza',
        back_populates='pizzas',
        overlaps="restaurant_pizzas"
    )

class RestaurantPizza(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    price = db.Column(db.Float)
    restaurant_id = db.Column(db.Integer, db.ForeignKey('restaurant.id'), nullable=False)
    pizza_id = db.Column(db.Integer, db.ForeignKey('pizza.id'), nullable=False)
    restaurant = db.relationship('Restaurant', backref=db.backref('restaurant_pizzas'), overlaps="restaurant_pizzas")
    pizza = db.relationship('Pizza', backref=db.backref('restaurant_pizzas'), overlaps="restaurant_pizzas")
