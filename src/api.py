from flask import Flask
from flask_restful import Api
from flask_jwt_extended import JWTManager

from database import db
from resources import login, registration, collections

# Create flask app
app = Flask(__name__)
api = Api(app)

# Configure flask app
app.config[
  "SECRET_KEY"] = "my name is ozymandius, king of kings:"  # TODO change this
app.config[
  "JWT_SECRET_KEY"] = "look on my works, ye mighty, and despair!"  # TODO change this
app.config[
  "SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"  # TODO testing DB only
app.config["SQLALCHEMY_COMMIT_ON_TEARDOWN"] = True

# Initialize flask app
db.init_app(app)
jwt = JWTManager(app)


# TODO testing DB only
@app.before_first_request
def create_tables():
  db.create_all()


# Add resources
api.add_resource(login.UserLogin, "/api/account/login")
api.add_resource(registration.UserRegistration, "/api/account/create")
api.add_resource(collections.Collections, "/api/collections")

if __name__ == "__main__":
  app.run(debug=True)