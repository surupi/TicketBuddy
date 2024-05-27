import io
from cache import cache
from flask import request, jsonify, send_file
from flask import current_app as app
from models import db
from common import allowed_file
from models import Customer, Admin, Movie, Venue, Booking, Category
from flask_jwt_extended import create_access_token, get_jwt_identity, jwt_required
from marsh_schema import MovieSchema, VenueSchema, BookingSchema, CustomerSchema, CategorySchema
from flask_mail import Message
# import mail
import datetime
import csv
from jobs import celery_app
from celery.result import AsyncResult
#__________________________________________________________________________________________________________________________




#Route to register
@app.route('/register', methods=['POST'])
def register():
    if request.is_json:
        data = request.get_json()
        if data['isAdmin'] == "user":
            userData = Customer(
                name=data['name'],
                phone=data['phone'],
                email=data['email'], 
                password=data['password'], 
                address=data['address'],
            )
        else:
            userData = Admin(
                name=data['name'],
                email=data['email'], 
                password=data['password'],
            )
        db.session.add(userData)
        db.session.commit()
        return {"message": f" {userData.name} has been registered successfully."}
    else:
        raise Exception("The request payload is not in JSON format")
    

#Route to update profile
@app.route('/updateprofile', methods=['PUT'])
def update_profile():
    if request.method == 'PUT':
        data = request.get_json()
        cust_id = data['cust_id']
        fields = (
            'name',
            'phone',
            'email', 
            'password', 
            'address',
        )
        for item in data.keys():
            if item in fields:
                db.session.query(Customer).filter_by(cust_id=cust_id).update(
                {
                    item: data[item]
                })
        db.session.commit()
        return {"message": f" Customer ID: {cust_id} has been updated successfully."}
    else:
        raise Exception("The request payload is not in JSON format")
    

#Route for user login
@app.route('/login', methods=['POST'])
def login():
    if request.is_json:
        email = request.json.get('email', None)
        password = request.json.get('password', None)

        if not email or not password:
           return {"error": "Missing email or password"}
        
        userData = Customer.query.filter_by(email=email).first()
        if userData is None:
            return {"error": "That user does not exist"}
        if userData.password != password:
            return {"error": "Invalid credentials"}
        else:
            access_token = create_access_token(identity={"email": email, "role": "user"}) 

            return {
                "cust_id": userData.cust_id, 
                "email": email, 
                "password": userData.password, 
                "name": userData.name, 
                "phone": userData.phone,
                "address": userData.address,
                "access_token": access_token
            }
    else:
        return {"error": "The request payload is not in JSON format"}


#Route for admin login
@app.route('/loginadmin', methods=['POST'])
def loginAdmin():
    if request.is_json:
        email = request.json.get('email', None)
        password = request.json.get('password', None)
        
        if not email or not password:
           return {"error": "Missing email or password"}
        # print (email, password)
        adminData = Admin.query.filter_by(email=email).first()
        if adminData is None:
            return {"error": "That admin does not exist"}
        if adminData.password != password:
            return {"error": "Invalid credentials"}
        else:
            access_token = create_access_token(identity={"email": email, "role": "admin"})
            return {"admin_id": adminData.admin_id, "email": email, "access_token": access_token}
    else:
        return {"error": "The request payload is not in JSON format"}
#__________________________________________________________________________________________________________________________

    
# Route to get all customers (ADMIN)
@app.route('/admincustomers', methods=['GET'])
@jwt_required()
@cache.cached(10)
def customers():
    print ("The cache is Working !!!!!!!!!!!!!!!!!!!!")
    user=get_jwt_identity()
    if user["role"] == "admin":
        customerData = Customer.query.all()
        return jsonify(CustomerSchema(many=True).dump(customerData))
    else:
        return {"message": "unauthorized"}, 401
#__________________________________________________________________________________________________________________________


# Route to get all customers (ADMIN)
@app.route('/adminbooking', methods=['GET'])
@jwt_required()
@cache.cached(10)
def mybooking():
    user=get_jwt_identity()
    if user["role"] == "admin":
        bookingData = Booking.query.all()
        return jsonify(BookingSchema(many=True).dump(bookingData))
    else:
        return {"message": "unauthorized"}, 401
#__________________________________________________________________________________________________________________________
    

# Route to get all categories (ADMIN)
@app.route('/admincategories', methods=['GET'])
@jwt_required()
@cache.cached(10)
def categories():
    user=get_jwt_identity()
    if user["role"] == "admin":
        categoryData = Category.query.all()
        return jsonify(CategorySchema(many=True).dump(categoryData))
    else:
        return {"message": "unauthorized"}, 401
    

# Route to delete a category (ADMIN)
@app.route('/deletecategory/<int:category_id>', methods=['DELETE'])
@jwt_required()
def delete_category(category_id):
    user=get_jwt_identity()
    if user["role"] == "admin":
        category = db.session.query(Category).filter_by(category_id=category_id)
        if category:
            category.delete()
            db.session.commit()
            return {"message": "Category successfully deleted"}
        else:
            return {"error": "Category not found"}
    else:
        return {"message": "unauthorized"}, 401
    

# Route to add categories (ADMIN)
@app.route('/adminaddcategory', methods=['POST'])
@jwt_required()
def add_category():
    user=get_jwt_identity()
    if user["role"] == "admin":
        if request.is_json:
            data = request.get_json()
            categoryData = Category(
                name=data['name'],
                description=data['description']
            )
            db.session.add(categoryData)
            db.session.commit()
            return {"message": "Category succesfully added"}
        else:
            return {"error": "The request payload is not in JSON format"}
    else:
        return {"message": "unauthorized"}, 401
    

# Route to modify a category (ADMIN)
@app.route('/modifycategory/<int:category_id>', methods=['PUT'])
@jwt_required()
def modify_category(category_id):
    user=get_jwt_identity()
    if user["role"] == "admin":
        if request.is_json:
            if category_id:
                data = request.get_json()
                fields = (
                    'name',
                    'description', 
                )
                for item in data.keys():
                    if item in fields:
                        print(data[item])
                        db.session.query(Category).filter_by(category_id=category_id).update(
                        {
                            item: data[item]
                        })
                db.session.commit()
                return {"message": "Category successfully modified"}
            else:
                return {"error": "Category not found"}
        else:
            return {"error": "The request payload is not in JSON format"}
    else:
        return {"message": "unauthorized"}, 401
#__________________________________________________________________________________________________________________________
    
    
# Route to get all venues (BOTH)
@app.route('/adminvenue', methods=['GET'])
@cache.cached(10)
def venue():
        venueData = Venue.query.all()
        return jsonify(VenueSchema(many=True).dump(venueData))


# Route to delete a venue (ADMIN)
@app.route('/deletevenue/<int:venue_id>', methods=['DELETE'])
@jwt_required()
def delete_venue(venue_id):
    user=get_jwt_identity()
    if user["role"] == "admin":
        venue = db.session.query(Venue).filter_by(venue_id=venue_id)
        if venue:
            venue.delete()
            db.session.commit()
            return {"message": "Venue successfully deleted"}
        else:
            return {"error": "Venue not found"}
    else:
        return {"message": "unauthorized"}, 401


# Route to add venue (ADMIN)
@app.route('/adminaddvenue', methods=['POST'])
@jwt_required()
def add_venue():
    user=get_jwt_identity()
    if user["role"] == "admin":
        if request.is_json:
            data = request.get_json()
            venueData = Venue(
                venue_name = data['venue_name'],
                venue_state = data['venue_state'],
                venue_city = data['venue_city']
            )
            db.session.add(venueData)
            db.session.commit()
            return {"message": "Venue succesfully added"}
        else:
            return {"error": "The request payload is not in JSON format"}
    else:
        return {"message": "unauthorized"}, 401


# Route to modify a venue (ADMIN)
@app.route('/modifyvenue/<int:venue_id>', methods=['PUT'])
@jwt_required()
def modify_venue(venue_id):
    user=get_jwt_identity()
    if user["role"] == "admin":
        if request.is_json:
            if venue_id:
                data = request.get_json()
                fields = (
                    'venue_name',
                    'venue_state',
                    'venue_city',
                )
                for item in data.keys():
                    if item in fields:
                        print(data[item])
                        db.session.query(Venue).filter_by(venue_id=venue_id).update(
                        {
                            item: data[item]
                        })
                db.session.commit()
                return {"message": "Venue successfully modified"}
            else:
                return {"error": "Venue not found"}
        else:
            return {"error": "The request payload is not in JSON format"}
    else:
        return {"message": "unauthorized"}, 401
#__________________________________________________________________________________________________________________________


# Route to get all movies (BOTH)
@app.route('/adminmovie', methods=['GET'])
@cache.cached(10)
def movie():
        movieData = Movie.query.all()
        result = []
        for movie in movieData:
            result.append({
                "category_name": movie.category.name,
                "category_id": movie.category_id,
                "movie_id": movie.movie_id,
                "movie_rating": movie.movie_rating,
                "movie_time": movie.movie_time,
                "name": movie.name,
                "number_of_seats": movie.number_of_seats,
                "ticket_price": movie.ticket_price,
                "venue_id": movie.venue_id
            })
        return jsonify(result)


# Route to delete a movie (ADMIN)
@app.route('/deletemovie/<int:movie_id>', methods=['DELETE'])
@jwt_required()
def delete_movie(movie_id):
    user=get_jwt_identity()
    if user["role"] == "admin":
        movie = db.session.query(Movie).filter_by(movie_id=movie_id)
        if movie:
            movie.delete()
            db.session.commit()
            return {"message": "Movie successfully deleted"}
        else:
            return {"error": "Movie not found"}
    else:
        return {"message": "unauthorized"}, 401
    

# Route to add movie (ADMIN)
@app.route('/adminaddmovie', methods=['POST'])
@jwt_required()
def add_movie():
    user=get_jwt_identity()
    if user["role"] == "admin":
        if request.is_json:
            data = request.get_json()
            movieData = Movie(
                name=data['name'],
                venue_id=data['venue_id'],
                movie_rating=data['movie_rating'],
                movie_time=datetime.datetime.strptime(data['movie_time'], "%Y-%m-%dT%H:%M"),
                category_id=data['category_id'],
                ticket_price=data['ticket_price'],
                number_of_seats=data['number_of_seats']
            )
            db.session.add(movieData)
            db.session.commit()
            return {"message": "Movie succesfully added"}
        else:
            return {"error": "The request payload is not in JSON format"}
    else:
        return {"message": "unauthorized"}, 401
    

# Route to modify a movie (ADMIN)
@app.route('/modifymovie/<int:movie_id>', methods=['PUT'])
@jwt_required()
def modify_movie(movie_id):
    user=get_jwt_identity()
    if user["role"] == "admin":
        if request.is_json:
            if movie_id:
                data = request.get_json()
                fields = (
                    'name',
                    'movie_rating',
                    'movie_time',
                    'category_id',
                    'ticket_price',
                    'number_of_seats',
                )
                if data["movie_time"].count(":") > 1:
                    data["movie_time"] = datetime.datetime.strptime(data['movie_time'][:-3], "%Y-%m-%dT%H:%M")
                else:
                    data["movie_time"] = datetime.datetime.strptime(data['movie_time'], "%Y-%m-%dT%H:%M")
                for item in data.keys():
                    if item in fields:
                        print(data[item])
                        # if item == "movie_time":
                        #     value = movie_time=datetime.datetime.strptime(data['movie_time'], "%Y-%m-%dT%H:%M")
                        db.session.query(Movie).filter_by(movie_id=movie_id).update(
                        {
                            item: data[item]
                        })
                db.session.commit()
                return {"message": "Movie successfully modified"}
            else:
                return {"error": "Movie not found"}
        else:
            return {"error": "The request payload is not in JSON format"}
    else:
        return {"message": "unauthorized"}, 401
#__________________________________________________________________________________________________________________________


# Route to get all venues (USER)
@app.route('/pickvenue', methods=['GET'])
@jwt_required()
@cache.cached(10)
def pickvenue():
    user=get_jwt_identity()
    if user["role"] == "user":
        pickvenueData = Venue.query.all()
        return jsonify(VenueSchema(many=True).dump(pickvenueData))
    else:
        return {"message": "unauthorized"}, 401


# Route to get all venues (USER)
@app.route('/pickmovie', methods=['GET'])
@jwt_required()
@cache.cached(10)
def pickmovie():
    user=get_jwt_identity()
    if user["role"] == "user":
        pickmovieData = Movie.query.all()
        result = []
        for movie in pickmovieData:
            result.append({
                "category_name": movie.category.name,
                "category_id": movie.category_id,
                "movie_id": movie.movie_id,
                "movie_rating": movie.movie_rating,
                "movie_time": movie.movie_time,
                "name": movie.name,
                "number_of_seats": movie.number_of_seats,
                "ticket_price": movie.ticket_price,
                "venue_id": movie.venue_id
            })
        return jsonify(result)
    else:
        return {"message": "unauthorized"}, 401


# Route to book a movie (USER)
@app.route('/useraddbooking/<int:movie_id_param>', methods=['POST'])
@jwt_required()
def add_booking(movie_id_param):
    user=get_jwt_identity()
    if user["role"] == "user":
        if request.is_json:
            data = request.get_json()
            cust_id = Customer.query.filter_by(email = user["email"]).first().cust_id
            tickets_needed = data['number_of_tickets']
            movie_id = movie_id_param
            current_movie = Movie.query.filter_by(movie_id = movie_id_param).first()
            venue_id = current_movie.venue_id
            bookingData = Booking(
                cust_id = cust_id,
                venue_id = venue_id,
                movie_id = movie_id,
                number_of_tickets = data['number_of_tickets'] ,
                date = datetime.date.today()
                
            )

            if (current_movie.number_of_seats !=0):
                if (current_movie.number_of_seats >= int(tickets_needed)):
                    current_movie.number_of_seats -= int(tickets_needed)
                    db.session.add(bookingData)
                    db.session.commit()
                    return {"message": "Booking succesfully added."}
                else:
                    return {"message": f"only {current_movie.number_of_seats} tickets left"}
            else:
                return {"message": "HOUSEFULL!! \n Sorry, there are no tickets left. Please consider watching another movie"}
        else:
            return {"error": "The request payload is not in JSON format"}
    else:
        return {"message": "unauthorized"}, 401
#__________________________________________________________________________________________________________________________


#Route to search venue (USER)
@app.route('/search_venue_keyword/<string:keyword>', methods=['GET'])
@jwt_required()
@cache.cached(10)
def search_venue_keyword(keyword):
    print (keyword)
    user=get_jwt_identity()
    if user["role"] == "user":
        # Query the database to find rows containing the keyword
        venueData = Venue.query.filter(Venue.venue_state.ilike(f"%{keyword}%")).all()
        if not venueData:
            return jsonify({"message": "No results found"})
        return jsonify(VenueSchema(many=True).dump(venueData))
    else:
        return {"message": "unauthorized"}, 401


#Route to search movie (USER)
@app.route('/search_movie_keyword/<string:keyword>', methods=['GET'])
@jwt_required()
@cache.cached(10)
def search_movie_keyword(keyword):
    user=get_jwt_identity()
    if user["role"] == "user":
        # Query the database to find rows containing the keyword
        movieData = Movie.query.filter(Movie.name.ilike(f"%{keyword}%")).all()
        result = []
        for movie in movieData:
            result.append({
                "category_name": movie.category.name,
                "category_id": movie.category_id,
                "movie_id": movie.movie_id,
                "movie_rating": movie.movie_rating,
                "movie_time": movie.movie_time,
                "name": movie.name,
                "number_of_seats": movie.number_of_seats,
                "ticket_price": movie.ticket_price,
                "venue_id": movie.venue_id
            })
        return jsonify(result)
    else:
        return {"message": "unauthorized"}, 401
#__________________________________________________________________________________________________________________________



#generate venue report as CSV
@celery_app.task
def generate_csv(venue_id):
    venues = Venue.query.filter_by(venue_id=venue_id).all()
    csv_file_path = 'venues.csv'
    csv_file = io.StringIO()
    writer = csv.writer(csv_file)
    writer.writerow(['venue_id', 'venue_name', 'venue_state', 'venue_city'])
    for venue in venues:
        writer.writerow([venue.venue_id, venue.venue_name, venue.venue_state, venue.venue_city])
    csv_file.seek(0)
    result = csv_file.read()
    # return (csv_file) for normal csv 
    return {"result": result} #for async csv


#export CSV async
@app.route('/exportcsvasync/<int:venue_id>', methods=['GET'])
def exportcsvasync(venue_id):
        result = generate_csv.delay(venue_id)
        return result.id
    

#export result
@app.route('/exportresult/<string:id>') 
def exportresult(id):
    result = AsyncResult(id, app=celery_app).result["result"]
    result = io.StringIO(result)
    file = io.BytesIO()
    file.write(result.getvalue().encode())
    file.seek(0)
    return send_file(file, as_attachment=True, download_name = "export.csv")
    

#Route to export csv (ADMIN)
@app.route('/exportcsv/<int:venue_id>', methods=['GET'])
@jwt_required()
def exportcsv(venue_id):
    user=get_jwt_identity()
    if user["role"] == "admin":
        result = generate_csv(venue_id)["result"]
        result = io.StringIO(result)
        file = io.BytesIO()
        file.write(result.getvalue().encode())
        file.seek(0)
        return send_file(file, as_attachment=True, download_name = "export.csv")
    else:
        return {"message": "unauthorized"}, 401