from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()

class User(db.Model):
    """Data model for a user"""

    __tablename__ = "users"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    fname = db.Column(db.String(20), nullable=False)
    lname = db.Column(db.String(25), nullable=False)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(25), nullable=False)

    favorites = db.relationship("Favorite", back_populates="user")

    def __repr__(self):
        return f"<user_id={self.id} email={self.email} first={self.fname} last={self.lname}>"


class Venue(db.Model):
    """Data model for venues."""

    __tablename__ = "venues"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    venue_name = db.Column(db.Text)
    external_id = db.Column(db.Text, nullable=False)
    phone = db.Column(db.Text)
    address = db.Column(db.Text)
    rating = db.Column(db.Text)
    review_count = db.Column(db.Text)

    favorites = db.relationship("Favorite", back_populates="venue")

    def __repr__(self):
        return f"<venue id={self.id}>"
    
    
class Favorite(db.Model):
    """Data model for user's Favorites."""

    __tablename__ = "favorites"

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    saved_at = db.Column(db.DateTime, default=datetime.utcnow)
    venue_id = db.Column(db.Integer, db.ForeignKey("venues.id"), nullable=False)

    user = db.relationship("User", back_populates="favorites")
    venue = db.relationship("Venue", back_populates="favorites")

    def __repr__(self):
        return f"<Favorite id={self.id} saved={self.saved_at}>"


def connect_to_db(app):
    """Connect the database to Flask app."""

    app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql:///test_db"
    app.config["SQLALCHEMY_ECHO"] = False
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    db.app = app
    db.init_app(app)
    print("Connected to db!")


if __name__ == "__main__":
    from flask import Flask

    app = Flask(__name__)
    connect_to_db(app)
    