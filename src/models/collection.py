from database import db
from sqlalchemy.orm import relationship

# Item model
class Item(db.Model):
  __tablename__ = "items"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  image_path = db.Column(db.String(120), nullable=False)
  collection_id = db.Column(db.Integer, db.ForeignKey("collections.id"), nullable=False)

# Collection model
class Collection(db.Model):
  __tablename__ = "collections"

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String(120), nullable=False)
  image_path = db.Column(db.String(120), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
  items = relationship("Item", backref="collections")