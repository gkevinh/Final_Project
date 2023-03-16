from flask import Flask, jsonify, render_template, request, redirect, session, flash, url_for
from model import connect_to_db, db
import crud, seed_database, model
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
GOOGLE_API_KEY = os.environ['GOOGLE_KEY']

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')


@app.route('/seed')
def seed_db():
    seed_database.seed()
    return 'done'


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
        flash("Account created. Please log in.")

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
        flash(f"Welcome back, {user.fname}")

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

    if not postal_code:
        message = "Please enter a zip code to search for venues."
        return render_template('search-form.html', message=message)


    url = 'https://api.yelp.com/v3/businesses/search'
    headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
    payload = {'limit': '30',
               'keyword': 'desserts',
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


@app.route('/venue/<id>')
def get_venue_details(id):
    """View the details of a venue."""

    url = f'https://api.yelp.com/v3/businesses/{id}'
    headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
    payload = {'apikey': YELP_API_KEY}

    user_email = session['user_email']
    user_by_email = crud.get_user_by_email(user_email)
    response = requests.get(url, params=payload, headers=headers).json()

    return render_template('venue-details.html',
                            business=response,
                            user=user_by_email)



@app.route('/map/directions/<id>')
def get_directions(id):
    """Creates map and directions."""
    url = f'https://api.yelp.com/v3/businesses/{id}'
    headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
    payload = {'apikey': YELP_API_KEY}

    response = requests.get(url, params=payload, headers=headers).json()

    return render_template("map.html",
                            business=response)


@app.route('/profile')
def view_profile():
    """View user's profile page."""
    
    user_email = session.get('user_email')
    if not user_email:
        flash('You must be logged in to view your profile.')
        return redirect('/')
    
    user = crud.get_user_by_email(user_email)
    favorites = user.favorites
    
    return render_template('profile.html', user=user, favorites=favorites)


# @app.route('/profile')
# def profile():
#     user_email = session['user_email']
#     user = crud.get_user_by_email(user_email)
#     favorites = crud.get_favorites_by_user(user)
#     return render_template('profile.html', user=user, favorites=favorites)


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



@app.route('/add-favorite', methods=['POST'])
def add_favorite():
    """Add a venue to user's favorites."""

    if 'user_email' not in session:
        return jsonify({'success': False, 'message': 'Please log in to add a favorite'})

    email = crud.get_user_by_email(session['user_email'])
    if not email:
        return jsonify({'success': False, 'message': 'Please log in to add a favorite'})

    venue_id = request.json.get('venue_id')
    venue = crud.get_venue_by_id(venue_id)
    if not venue:
        return jsonify({'success': False, 'message': 'Venue not found'})

    favorite = crud.save_as_favorite(email, venue_id)
    db.session.add(favorite)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Added to favorites!'})



@app.route('/remove-favorite', methods=['DELETE'])
def remove_favorite():
    """Remove a venue from user's favorites."""

    if 'user_email' not in session:
        return jsonify({'success': False, 'message': 'Please log in to remove a favorite'})

    user = crud.get_user_by_email(session['user_email'])
    if not user:
        return jsonify({'success': False, 'message': 'Please log in to remove a favorite'})

    venue_id = request.json.get('venue_id')
    venue = crud.get_venue_by_id(venue_id)
    if not venue:
        return jsonify({'success': False, 'message': 'Venue not found'})

    favorite = crud.remove_favorite(venue_id)
    if not favorite:
        return jsonify({'success': False, 'message': 'Favorite not found'})
    db.session.delete(favorite)
    db.session.commit()
    return jsonify({'success': True, 'message': 'Removed from favorites!'})





# @app.route('/remove_favorite/<int:id>', methods=["POST"])
# def remove_favorite(id):
#     """Remove favorite from Favorites."""
    
#     favorite = crud.get_favorite_by_id(id)

#     if not favorite:
#         flash("Favorite not found.")
#     else:
#         crud.delete_favorite(favorite)
#         flash("Favorite removed.")

#     return redirect("/")



@app.route('/logout')
def logout():
    """Logout"""

    session.pop('user')
    flash('You are now logged out.')
    return redirect("/")



if __name__ == "__main__":
    connect_to_db(app)
    print("http://localhost:5000/")
    app.run(host="0.0.0.0", debug=True)