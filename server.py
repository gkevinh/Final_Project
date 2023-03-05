from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud
import os
import requests
from pprint import pprint
from pprint import pformat
import json

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "key"
app.jinja_env.undefined = StrictUndefined

YELP_API_KEY = os.environ['YELP_KEY']

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


# @app.route("/users")
# def all_users():
#     """View all movies."""

#     users = crud.get_users()

#     return render_template("all_users.html", users=users)


@app.route("/user", methods=["POST"])
def register_user():
    """Create a new user."""

    fname = request.form.get("fname")
    lname = request.form.get("lname")
    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if user:
        flash("Cannot create an account with that email. Try again.")
    else:
        user = crud.create_user(fname, lname, email, password)
        db.session.add(user)
        db.session.commit()
        flash("Account created! Please log in.")

    return redirect("/")


@app.route("/login", methods=["POST"])
def process_login():
    """Process user login."""

    email = request.form.get("email")
    password = request.form.get("password")

    user = crud.get_user_by_email(email)
    if not user or user.password != password:
        flash("The email or password you entered was incorrect.")
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.fname}!")

    return redirect("/")



# @app.route('/venue')
# def show_search_form():
#     """Show search form"""

#     return render_template('search-form.html')


# @app.route('/venues/search')
# def find_venues():
#     """Search for dessert places"""

#     keyword = request.args.get('keyword', '')
#     postal_code = request.args.get('zip_code', '')
#     radius = request.args.get('radius', '')
#     sort = request.args.get('sort', '')

#     url = 'https://api.yelp.com/v3/businesses/search'
#     payload = {'apikey': YELP_API_KEY,
#                'keyword': 'desserts',
#                'postal_code': postal_code,
#                'radius': radius,
#                'sort': sort}

#     response = requests.get(url, params=payload)
#     data = response.json()

#     if '_embedded' in data:
#         businesses = data['_embedded']['businesses']
#     else:
#         businesses = []

#     return render_template('search-results.html',
#                            pformat=pformat,
#                            data=data,
#                            results=businesses)



# @app.route('/event/<id>')
# def get_event_details(id):
#     """View the details of an event."""

#     url = f'https://app.ticketmaster.com/discovery/v2/events/{id}'
#     payload = {'apikey': API_KEY}

#     response = requests.get(url, params=payload)
#     event = response.json()

#     if '_embedded' in event:
#         venues = event['_embedded']['venues']
#     else:
#         venues = []

#     return render_template('event-details.html',
#                            event=event,
#                            venues=venues)





# @app.route('/')
# def homepage():
#     """Show homepage."""

#     return render_template('homepage.html')


# @app.route('/afterparty')
# def show_afterparty_form():
#     """Show event search form"""

#     return render_template('search-form.html')


# @app.route('/venues/search')
# def call_yelp_api():
#     """Search for venues"""

#     endpoint = "https://api.yelp.com/v3/businesses/search"
#     headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
#     payload = {'limit' : '15', 'location' : '90404', 'categories' : 'desserts'}

#     response = requests.get(endpoint, params=payload, headers=headers).json()

#     pprint(response['businesses'])

    # business_data = response.json()

    # print(json.dumps(business_data, indent = 3))






#-------------

# @app.route("/")
# def homepage():
#     """View homepage."""

#     return render_template("homepage.html")


# @app.route("/movies")
# def all_movies():
#     """View all movies."""

#     movies = crud.get_movies()

#     return render_template("all_movies.html", movies=movies)


# @app.route("/movies/<movie_id>")
# def show_movie(movie_id):
#     """Show details on a particular movie."""

#     movie = crud.get_movie_by_id(movie_id)

#     return render_template("movie_details.html", movie=movie)


# @app.route("/users")
# def all_users():
#     """View all users."""

#     users = crud.get_users()

#     return render_template("all_users.html", users=users)




#     return redirect("/")


# @app.route("/users/<user_id>")
# def show_user(user_id):
#     """Show details on a particular user."""

#     user = crud.get_user_by_id(user_id)

#     return render_template("user_details.html", user=user)



# @app.route("/update_rating", methods=["POST"])
# def update_rating():
#     rating_id = request.json["rating_id"]
#     updated_score = request.json["updated_score"]
#     crud.update_rating(rating_id, updated_score)
#     db.session.commit()

#     return "Success"

# @app.route("/movies/<movie_id>/ratings", methods=["POST"])
# def create_rating(movie_id):
#     """Create a new rating for the movie."""

#     logged_in_email = session.get("user_email")
#     rating_score = request.form.get("rating")

#     if logged_in_email is None:
#         flash("You must log in to rate a movie.")
#     elif not rating_score:
#         flash("Error: you didn't select a score for your rating.")
#     else:
#         user = crud.get_user_by_email(logged_in_email)
#         movie = crud.get_movie_by_id(movie_id)

#         rating = crud.create_rating(user, movie, int(rating_score))
#         db.session.add(rating)
#         db.session.commit()

#         flash(f"You rated this movie {rating_score} out of 5.")

#     return redirect(f"/movies/{movie_id}")


if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)