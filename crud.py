"""CRUD operations."""

from model import db, User, Favorite, Venue, connect_to_db
from datetime import datetime


def create_user(fname, lname, email,password):
    """Create and return a new user."""
    user = User(fname=fname, lname=lname, email=email, password=password)
    return user


def get_user_by_id(id):
    """Return a user by primary key."""
    return User.query.get(id)


def get_user_by_email(email):
    """Return a user by email."""
    return User.query.filter(User.email == email).first()


def get_users():
    """Return all users."""
    return User.query.all()


def get_venue_by_id(id):
    """Return a venue by primary key."""
    return Venue.query.get(id)


def get_venue_by_external_id(external_id):
    """Return a venue by external id."""
    return Venue.query.get(external_id)


def get_favorites():
    """Return all favorites."""
    return Favorite.query.all()


def save_as_favorite(user, venue):
    """Save and return a favorite."""
    favorite = Favorite(user=user, venue=venue)
    return favorite


def get_venue_by_external_id(external_id):
    """Return a venue by external ID."""
    return Venue.query.filter_by(external_id=external_id).first()


def get_favorite_by_user_and_venue(user, venue):
    """Return favorite object given user and venue."""
    return Favorite.query.filter_by(user=user, venue=venue).first()



def get_favorite_by_id(id):
    """Return favorite by id."""
    return Favorite.query.filter_by(id=id).first()



def create_venue(venue_name, external_id):
    db_venue = Venue(venue_name=venue_name, external_id=external_id)
    db.session.add(db_venue)
    db.session.commit()
    return db_venue    
    
if __name__ == "__main__":
    from server import app
    connect_to_db(app)