from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

# Admin Table
class Admin(db.Model):
    __tablename__ = 'admin'

    admin_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique = True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)

    def __init__(self, email, password, name):
        self.email = email
        self.password = password
        self.name = name


# Booking Table
class Booking(db.Model):
    __tablename__ = 'booking'

    booking_id = db.Column(db.Integer, primary_key=True)
    cust_id = db.Column(db.Integer, db.ForeignKey('customer.cust_id', ondelete='cascade'), nullable=False)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.venue_id', ondelete='cascade'), nullable=False)
    movie_id = db.Column(db.Integer, db.ForeignKey('movie.movie_id', ondelete='cascade'), nullable=False)
    number_of_tickets = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)
    venue=db.relationship("Venue")

    def __init__(self, cust_id, venue_id, movie_id, number_of_tickets, date):
        self.cust_id = cust_id
        self.venue_id = venue_id
        self.movie_id = movie_id
        self.number_of_tickets = number_of_tickets
        self.date=date


# Category Table
class Category(db.Model):
    __tablename__ = 'category'

    category_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    description = db.Column(db.String(255), nullable=False)
        
    def __init__(self, name, description):
        self.name = name
        self.description = description


# Customer Table
class Customer(db.Model):
    __tablename__ = 'customer'

    cust_id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(30), unique = True, nullable=False)
    password = db.Column(db.String(30), nullable=False)
    name = db.Column(db.String(30), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone = db.Column(db.Numeric(10), nullable=False)

    def __init__(self, email, password, name, address, phone):
        self.email = email
        self.password = password
        self.name = name
        self.address = address
        self.phone = phone


# Movie Table
class Movie(db.Model):
    __tablename__ = 'movie'

    movie_id = db.Column(db.Integer, primary_key=True)
    venue_id = db.Column(db.Integer, db.ForeignKey('venue.venue_id', ondelete='cascade'), nullable=False)
    name = db.Column(db.Unicode(30), nullable=False)
    movie_rating = db.Column(db.Numeric(4), nullable=False)
    movie_time = db.Column(db.DateTime(), nullable=False)
    category_id = db.Column(db.Integer, db.ForeignKey('category.category_id', ondelete='cascade'), nullable=False)
    category = db.relationship("Category")
    ticket_price = db.Column(db.Numeric(10, 2), nullable=False)
    number_of_seats =  db.Column(db.Integer, nullable=False)

    def __init__(self, name, venue_id, movie_rating, movie_time, category_id, ticket_price, number_of_seats):
        self.name = name
        self.venue_id = venue_id
        self.movie_rating = movie_rating
        self.movie_time = movie_time
        self.category_id = category_id
        self.ticket_price = ticket_price
        self.number_of_seats = number_of_seats


# Venue Table
class Venue(db.Model):
    __tablename__ = 'venue'

    venue_id = db.Column(db.Integer, primary_key=True)
    venue_name = db.Column(db.Unicode(30), nullable=False)
    venue_state = db.Column(db.String(20), nullable=False)
    venue_city = db.Column(db.String(20), nullable=False)
    
    def __init__(self, venue_name, venue_state, venue_city):
        self.venue_name = venue_name
        self.venue_state = venue_state
        self.venue_city = venue_city
