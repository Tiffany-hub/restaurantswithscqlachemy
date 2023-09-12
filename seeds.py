from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base, Restaurant, Customer, Review

# Create an engine that connects to the database
engine = create_engine('sqlite:///restaurant.db')

# Create all tables
Base.metadata.create_all(bind=engine)

# Create a session
Session = sessionmaker(bind=engine)
session = Session()

# Add some sample data
restaurant1 = Restaurant(name="Restaurant A", price=3)
restaurant2 = Restaurant(name="Restaurant B", price=2)

customer1 = Customer(first_name="John", last_name="Doe")
customer2 = Customer(first_name="Jane", last_name="Smith")

review1 = Review(rating=4, comment="Great food!", customer=customer1, restaurant=restaurant1)
review2 = Review(rating=5, comment="Excellent service!", customer=customer2, restaurant=restaurant2)

# Add objects to the session
session.add_all([restaurant1, restaurant2, customer1, customer2, review1, review2])

# Commit the session to save changes to the database
session.commit()

# Close the session
session.close()
