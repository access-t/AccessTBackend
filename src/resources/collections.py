from flask_jwt_extended.utils import get_jwt_identity
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from models.user import User
from models.collection import Collection

# Request body parser for collections GET resource
parser_get = reqparse.RequestParser()
parser_get.add_argument("name")

# Request body parser for collections POST resource
parser_post = reqparse.RequestParser()
parser_post.add_argument("collection_name",
                         help="This field cannot be blank",
                         required=True)
parser_post.add_argument("image_path",
                         help="This field cannot be blank",
                         required=True)


# User collections resource
# Endpoint: /api/collections
class Collections(Resource):

  @jwt_required
  def get(self):
    data = parser_get.parse_args()
    name = data["name"]
    if not name:
      return Collection.return_all(get_jwt_identity())
    return Collection.return_by_name(get_jwt_identity(), name)

  @jwt_required
  # TODO this will let you create multiple collections with the same name.
  # I can enforce a unique constraint on this, or I could not?
  # Do more thinking about if we want to allow multiple collections with the same name
  def post(self):
    data = parser_post.parse_args()
    collection_name = data["collection_name"]
    image_path = data["image_path"]
    username = get_jwt_identity()
    user = User.find_by_username(username)

    if not user:
      return {"message": "User {} doesn't exist".format(username)}, 500

    user.collections.append(
      Collection(name=collection_name, image_path=image_path))

    try:
      user.save_to_db()
      return {
        "message": "Collection {} was added".format(collection_name),
      }
    except:
      return {"message": "Could not add new collection"}, 500