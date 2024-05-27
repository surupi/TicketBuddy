from flask import Flask, request
from flask_cors import CORS
from flask_migrate import Migrate
from flask_jwt_extended import JWTManager
from flask_mail import Mail #,Message
import os
from cache import cache
import redis
from models import db
from flask_sqlalchemy import inspect



#creates a Flask web application, sets up the application context, imports route definitions from a module called routes
def create_app():
    app = Flask(__name__)
    with app.app_context():
        import routes
    return app


app = create_app()
mail = Mail(app)
app.debug = True
SQLALCHEMY_TRACK_MODIFICATIONS = False

# Image uploading
UPLOAD_FOLDER = '../images'

app.config['CORS_HEADERS'] = 'Content-Type'
app.config['JWT_SECRET_KEY'] = 'ssssss'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

app.config["CACHE_TYPE"] = "RedisCache"
app.config['CACHE_REDIS_HOST'] = "localhost"
app.config['CACHE_REDIS_PORT'] = 6379
app.config["CACHE_REDIS_URL"] = "redis://localhost:6379"  
app.config['CACHE_DEFAULT_TIMEOUT'] = 200


#IS THIS USED??
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///test.sqlite3'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
SMPTP_SERVER_HOST = "localhost"
SMPTP_SERVER_PORT = 1025
SENDER_ADDRESS = ""
SENDER_PASSWORD=""


app.app_context().push()
CORS(app)
cache.init_app(app)
app.config.update(
    CELERY_BROKER_URL="redis://localhost:6379/0",
    CELERY_RESULT_BACKEND="redis://localhost:6379/1"
)


# configuration of database
app.config.from_object(__name__)

db.init_app(app) #initialize the application
with app.app_context():
    if not (inspect(db.engine).has_table("admin")):
        from models import Admin
        db.create_all() #create tables
        admin=Admin("admin@gmail.com", "1234567890", "admin")
        db.session.add(admin)
        db.session.commit()

#= SQLAlchemy(app)
migrate = Migrate(app, db)

jwt = JWTManager(app)


if __name__ == "__main__":
    app.run(debug = True)

