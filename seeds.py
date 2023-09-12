from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Create an engine and bind it to the Base class
engine = create_engine('sqlite:///restaurant.db')
Base.metadata.bind = engine

# Create a session
DBSession = sessionmaker(bind=engine)
session = DBSession()

# Create instances
restaurant1 = Restaurant(name="Restaurant A", price=3)
customer1 = Customer(first_name="John", last_name="Doe")
review1 = Review(rating=5, customer=customer1, restaurant=restaurant1)

# Add instances to the session
session.add(restaurant1)
session.add(customer1)
session.add(review1)

# Commit the session to save the data to the database
session.commit()
