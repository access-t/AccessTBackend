from database import db
from models.user import User
from sqlalchemy.orm import relationship


# Item model
class Item(db.Model):
  __tablename__ = "items"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  image_path = db.Column(db.String(120), nullable=False)
  collection_id = db.Column(db.Integer,
                            db.ForeignKey("collections.id"),
                            nullable=False)


# Collection model
class Collection(db.Model):
  __tablename__ = "collections"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  image_path = db.Column(db.String(120), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
  items = relationship("Item", backref="collections")

  @classmethod
  def return_by_name(cls, username, collection_name):

    def to_json(x):
      return {"name": x.name, "image_path": x.image_path}

    user = User.find_by_username(username)
    return {
      "collections":
        list(
          map(lambda x: to_json(x),
              Collection.query.filter_by(user_id=user.id, name=collection_name)))
    }

  @classmethod
  def return_all(cls, username):

    def to_json(x):
      return {"name": x.name, "image_path": x.image_path}

    user = User.find_by_username(username)
    return {
      "collections":
        list(
          map(lambda x: to_json(x),
              Collection.query.filter_by(user_id=user.id)))
    }