from flask import (Flask, render_template, request, flash, session,
                   redirect)
from model import connect_to_db, db
import crud, seed_database
import os
import requests
# from pprint import pprint
from pprint import pformat
import json

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "key"
app.jinja_env.undefined = StrictUndefined

YELP_API_KEY = os.environ['YELP_KEY']
GOOGLE_API_KEY = os.environ['GOOGLE_KEY']

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/seed')
def seed_db():
    seed_database.seed()
    return 'done'
    
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


@app.route('/venue')
def show_search_form():
    """Show search form"""

    return render_template('search-form.html')


@app.route('/venues/search')
def find_venues():
    """Search for dessert places"""

    keyword = request.args.get('keyword', '')
    postal_code = request.args.get('zipcode', '')
    radius = request.args.get('radius', '')
    sort = request.args.get('sort', '')

    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
    payload = {'limit': '30',
               'keyword': keyword,
               'term': 'desserts',
               'location': postal_code,
               'radius': radius,
               'sort': sort}

    response = requests.get(url, params=payload, headers=headers).json()

    if 'businesses' in response:
        businesses = response['businesses']
    else:
        businesses = []

    return render_template('search-results.html',
                           pformat=pformat,
                           data=response,
                           businesses=businesses)


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





# @app.route("/favorites")
# def all_favorites():
#     """View all favorites."""

#     favorites = crud.get_favorites()



# # @app.route("/users/<user_id>")
# # def show_user(user_id):
# #     """Show details on a particular user."""

# #     user = crud.get_user_by_id(user_id)

# #     return render_template("user_details.html", user=user)


@app.route("/map/directions")
def get_directions():
    """Demo of basic map-related code.

    - Programmatically adding markers, info windows, and event handlers to a
      Google Map
    - Showing polylines, directions, etc.
    """

    return render_template("map.html")


@app.route("/map/basic")
def view_basic_map():
    """Demo of basic map-related code.

    - Programmatically adding markers, info windows, and event handlers to a
      Google Map
    - Showing polylines, directions, etc.
    """

    return render_template("map-basic.html")


@app.route("/map/more")
def view_more_demos():
    """Demo of basic map-related code.

    - Programmatically adding markers, info windows, and event handlers to a
      Google Map
    - Showing polylines, directions, etc.
    """

    return render_template("map-more.html")



if __name__ == "__main__":
    connect_to_db(app)
    app.run(host="0.0.0.0", debug=True)