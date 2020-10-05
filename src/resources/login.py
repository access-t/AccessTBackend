from models.user import User
from flask_restful import Resource, reqparse
from flask_jwt_extended import create_access_token, create_refresh_token

# Request body parser for login resource
parser = reqparse.RequestParser()
parser.add_argument("username",
                    help="This field cannot be blank",
                    required=True)
parser.add_argument("password",
                    help="This field cannot be blank",
                    required=True)


# User login resource
# Endpoint: /api/account/login
class UserLogin(Resource):

  def post(self):
    data = parser.parse_args()
    username = data["username"]
    user = User.find_by_username(username)

    if not user:
      return {"message": "User {} doesn't exist".format(username)}, 500

    if User.verify_hash(data["password"], user.password):
      access_token = create_access_token(identity=username)
      refresh_token = create_refresh_token(identity=username)
      return {
        "message": "Logged in as {}".format(user.username),
        "access_token": access_token,
        "refresh_token": refresh_token
      }
    else:
      return {"message": "Invalid username or password"}, 500