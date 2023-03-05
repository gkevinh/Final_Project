"""Script to seed database."""

import os
import json
from random import choice, randint
from datetime import datetime

import crud
import model
import server

os.system("dropdb test_db")
os.system("createdb test_db")

model.connect_to_db(server.app)
model.db.create_all()

# Load user data from JSON file
with open("data/users.json") as f:
    user_data = json.loads(f.read())

# Load venue data from JSON file
with open("data/venues.json") as g:
    venue_data = json.loads(g.read())


# Create users

users_in_db = []
for user in user_data:
    fname, lname, password, email = (
        user["fname"],
        user["lname"],
        user["password"],
        user["email"],
    )

    db_user = crud.create_user(fname, lname, password, email)
    users_in_db.append(db_user)

model.db.session.add_all(users_in_db)
model.db.session.commit()

# Create venues

venues_in_db = []
for venue in venue_data:
    venue_name, external_id = (
        venue["venue_name"],
        venue["external_id"],
    )

    db_venue = crud.create_venue(venue_name, external_id)
    venues_in_db.append(db_venue)

model.db.session.add_all(venues_in_db)
model.db.session.commit()

# Create favorites

# favorites_in_db = []
# for fav in favorite_data:
#     user_id, venue_id, notes = (
#         fav["user_id"],
#         fav["venue_id"],
#         fav["notes"],
#     )

#     db_favorite = crud.save_as_favorite(user.id, venue.id, notes)
#     favorites_in_db.append(db_favorite)

# model.db.session.add_all(favorites_in_db)
# model.db.session.commit()

for n in range(1,4):
    favorite_venue = randint(1, 3)
    favorite = crud.save_as_favorite(user_id=n, venue_id=favorite_venue, notes="test notes")
    model.db.session.add(favorite)

model.db.session.commit()
