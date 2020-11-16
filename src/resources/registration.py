from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token

from models.user import User

# Request body parser for registration resource
parser = reqparse.RequestParser()
parser.add_argument("first_name",
                    help="This field cannot be blank",
                    required=True)
parser.add_argument("last_name",
                    help="This field cannot be blank",
                    required=True)
parser.add_argument("email", help="This field cannot be blank", required=True)
parser.add_argument("username",
                    help="This field cannot be blank",
                    required=True)
parser.add_argument("password",
                    help="This field cannot be blank",
                    required=True)


# User registration resource
# Endpoint: /api/account/create
class UserRegistration(Resource):

  def post(self):
    data = parser.parse_args()
    username = data["username"]
    password = data["password"]

    if User.find_by_username(username):
      return {"message": "User {} already exists".format(username)}, 500

    new_user = User(first_name=data["first_name"],
                    last_name=data["last_name"],
                    email=data["email"],
                    username=username,
                    password=User.generate_hash(password))

    try:
      new_user.save_to_db()
      access_token = create_access_token(identity=username, expires_delta=False)
      return {
        "message": "User {} was created".format(username),
        "access_token": access_token
      }
    except:
      return {"message": "Could not register user"}, 500