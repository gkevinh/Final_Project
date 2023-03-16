"""CRUD operations."""

from model import db, User, Favorite, Venue, connect_to_db
from datetime import datetime
from flask import Flask, render_template, request, redirect, session, flash



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


def get_favorites():
    """Return all favorites."""

    return Favorite.query.all()


def save_as_favorite(email, external_id):
    """Save and return a favorite."""

    favorite = Favorite(email=email, external_id=external_id)

    return favorite


def get_venue_by_external_id(external_id):
    """Return a venue by external ID."""

    return Venue.query.filter(Venue.external_id == external_id).first()



def remove_favorite(venue_id):
    """ Remove favorite from Favorites. """
    favorite = Favorite.query.filter(Favorite.venue_id == id).first()

    if not favorite:
        flash("Favorite not found.")
    else:
        db.session.delete(favorite)
        db.session.commit()
        flash("Favorite removed.")

    return redirect("/")



if __name__ == "__main__":
    from server import app
    connect_to_db(app)