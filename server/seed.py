from faker import Faker
from flask import Flask
from models import db, Restaurant, Pizza, RestaurantPizza

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

fake = Faker()

def generate_fake_data(num_restaurants, num_pizzas_per_restaurant):
    with app.app_context():
        for _ in range(num_restaurants):
            restaurant = Restaurant(
                name=fake.company(),
                address=fake.address()
            )
            db.session.add(restaurant)

            for _ in range(num_pizzas_per_restaurant):
                pizza = Pizza(
                    name=fake.word(),
                    ingredients=fake.sentence()
                )
                db.session.add(pizza)
                db.session.flush()

                restaurant_pizza = RestaurantPizza(
                    price=fake.random_number(digits=2),
                    restaurant_id=restaurant.id,
                    pizza_id=pizza.id
                )
                db.session.add(restaurant_pizza)

        db.session.commit()

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        generate_fake_data(10, 5)