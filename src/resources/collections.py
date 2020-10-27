from flask_jwt_extended.utils import get_jwt_identity
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required

from models.user import User
from models.collection import Collection, Item

import werkzeug, util

# Request body parser for collections GET resource
parser_get = reqparse.RequestParser()
parser_get.add_argument("name")

# Request body parser for collections POST resource
parser_post = reqparse.RequestParser()
parser_post.add_argument("collection_name",
                         help="collection_name field cannot be blank",
                         required=True)
parser_post.add_argument("image",
                         type=werkzeug.datastructures.FileStorage,
                         help="image field cannot be blank",
                         location="files",
                         required=True)

# Request body parser for collections PUT resource
parser_put = reqparse.RequestParser()
parser_put.add_argument("collection_name",
                        help="collection_name field cannot be blank",
                        required=True)
parser_put.add_argument("name",
                        help="name field cannot be blank",
                        required=True)
parser_put.add_argument("image",
                         type=werkzeug.datastructures.FileStorage,
                         help="image field cannot be blank",
                         location="files",
                         required=True)


# User collections resource
# Endpoint: /api/collections
class Collections(Resource):

  @jwt_required
  def get(self):
    # TODO we need to return the image here
    data = parser_get.parse_args()
    name = data["name"]
    if not name:
      return Collection.return_all(get_jwt_identity())
    return Collection.return_by_name(get_jwt_identity(), name)

  @jwt_required
  def post(self):
    data = parser_post.parse_args()
    collection_name = data["collection_name"]
    image_name = "{}.{}".format(collection_name, "jpg")
    image_file = data["image"]
    username = get_jwt_identity()
    user = User.find_by_username(username)

    if not user:
      return {"message": "User {} doesn't exist".format(username)}, 500

    if Collection.query.filter_by(user_id=user.id,
                                  name=collection_name).count() > 0:
      return {
        "message": "Collection {} already exists".format(collection_name)
      }, 500

    try:
      user.collections.append(
        Collection(name=collection_name, image_path=image_name))
      util.save_file(image_file, [username, collection_name], image_name)
      user.save_to_db()
      return {
        "message": "Collection {} was added".format(collection_name),
      }
    except:
      return {"message": "Could not add collection"}, 500

  @jwt_required
  def put(self):
    data = parser_put.parse_args()
    collection_name = data["collection_name"]
    name = data["name"]
    image_name = "{}.{}".format(name, "jpg")
    image_file = data["image"]
    username = get_jwt_identity()
    user = User.find_by_username(username)

    if not user:
      return {"message": "User {} doesn't exist".format(username)}, 500

    collection = Collection.query.filter_by(user_id=user.id,
                                            name=collection_name).first()
    
    if collection is None:
      return {"message": "Collection {} doesn't exist".format(collection_name)}, 500

    if collection.items.filter(Item.name == name).count() > 0:
      return {"message": "Item with name {} already exists".format(name)}, 500

    try:
      collection.items.append(Item(name=name, image_path=image_name))
      util.save_file(image_file, [username, collection_name, "items"], image_name)
      collection.save_to_db()
      return {
        "message": "Collection {} was updated".format(collection_name),
      }
    except:
      return {"message": "Could not update collection"}, 500