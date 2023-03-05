"""CRUD operations."""

from model import db, User, Favorite, Venue, connect_to_db
from datetime import datetime


def create_user(fname, lname, email,password):
    """Create and return a new user."""

    user = User(fname=fname, lname=lname, email=email, password=password)
    # db.session.add(user)
    # db.session.commit()
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


def create_venue(venue_name, external_id):
    """Create and return a new venue."""

    venue = Venue(venue_name=venue_name, external_id=external_id)

    return venue


def get_all_venues():
    """Return all venues."""

    return Venue.query.all()


def get_venue_by_id(id):
    """Return a venue by primary key."""

    return Venue.query.get(id)


def get_favorites():
    """Return all favorites."""

    return Favorite.query.all()


def save_as_favorite(user_id, venue_id, notes):
    """Save and return a favorite."""

    favorite = Favorite(user_id=user_id, venue_id=venue_id, notes=notes)

    return favorite


# def remove_favorite(id):
#     """ Remove favorite from Favorites. """
#     # create "Are you sure you want to delete?"
#     favorite = Favorite.query.filter(id).delete()
#     db.session.commit()

#     Favorite.query.filter_by(favorites.id).delete()


if __name__ == "__main__":
    from server import app
    connect_to_db(app)