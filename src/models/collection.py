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

  # For serializing to JSON
  def as_dict(self):
    return {"name": self.name, "image_path": self.image_path}


# Collection model
class Collection(db.Model):
  __tablename__ = "collections"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  image_path = db.Column(db.String(120), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
  items = relationship("Item", backref="collections")

  # For serializing to JSON
  def as_dict(self):
    return {
      "name": self.name,
      "image_path": self.image_path,
      "items": [item.as_dict() for item in self.items]
    }

  @classmethod
  def return_by_name(cls, username, collection_name):

    user = User.find_by_username(username)
    return {
      "collections":
        list(
          map(lambda x: x.as_dict(),
              Collection.query.filter_by(user_id=user.id,
                                         name=collection_name)))
    }

  def save_to_db(self):
    db.session.add(self)
    db.session.commit()

  @classmethod
  def return_all(cls, username):

    user = User.find_by_username(username)
    return {
      "collections":
        list(
          map(lambda x: x.as_dict(),
              Collection.query.filter_by(user_id=user.id)))
    }