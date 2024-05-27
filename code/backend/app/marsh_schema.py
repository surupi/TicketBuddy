from marshmallow import Schema

class AdminSchema(Schema):
    class Meta:
        fields = ('admin_id', 'email', 'password', 'name')

class BookingSchema(Schema):
    class Meta:
        fields = ('booking_id', 'cust_id', 'venue_id', 'movie_id', 'number_of_tickets')

class CategorySchema(Schema):
    class Meta:
        fields = ('category_id', 'name', 'description')

class CustomerSchema(Schema):
    class Meta:
        fields = ('cust_id', 'email', 'password', 'name', 'address', 'phone')

class MovieSchema(Schema):
    class Meta:
        fields = ('movie_id', 'venue_id', 'name', 'movie_rating', 'movie_time', 'category_id', 'ticket_price', 'number_of_seats')   
        
class VenueSchema(Schema):
    class Meta:
        fields = ('venue_id', 'venue_name', 'venue_state', 'venue_city') 