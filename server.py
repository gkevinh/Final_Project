from flask import Flask, jsonify, render_template, request, redirect, session, flash, url_for
from model import connect_to_db, db, Venue, User, Favorite
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
GOOGLE_API_KEY = os.environ['GOOGLE_KEY']

@app.route('/')
def homepage():
    """View homepage."""

    return render_template('homepage.html')



@app.route('/create_account')
def create_account():
    """Create user account."""

    return render_template('create-account.html')



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
        return render_template('create-account.html')
    
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
        flash("Information was incorrect.")
        return redirect("/")
        
       
    else:
        # Log in user by storing the user's email in session
        session["user_email"] = user.email
        flash(f"Welcome back, {user.fname}")
        return redirect("/venue")
    
    
    
@app.route('/venue')
def show_search_form():
    """Show search form"""

    if 'user_email' not in session:
        flash('You need to log in to view venue details.')
        return redirect('/')
    
    return render_template('search-form.html')


@app.route('/venues/search')
def find_venues():
    """Search for dessert places"""

    if 'user_email' not in session:
        flash('You need to log in to view venue details.')
        return redirect('/')

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

    if 'user_email' not in session:
        flash('You need to log in to view venue details.')
        return redirect('/')

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

    if 'user_email' not in session:
        flash('You need to log in to view map details.')
        return redirect('/')

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


@app.route('/add-favorite', methods=['POST'])
def add_favorite():
    """Add a venue to user's favorites."""
    if 'user_email' not in session:
        return jsonify({'success': False, 'message': 'Please log in to add a favorite'})

    user = crud.get_user_by_email(session['user_email'])
    if not user:
        return jsonify({'success': False, 'message': 'Please log in to add a favorite'})

    data = request.json
    external_id = data.get('external_id')
    venue_name = data.get('venue_name')
    phone = data.get('phone')
    address = data.get('address')
    rating = data.get('rating')
    review_count = data.get('review_count')
    user_id = user.id

    venue = crud.get_venue_by_external_id(external_id)
    if not venue:
        venue = Venue(venue_name=venue_name,
                      external_id=external_id,
                      phone=phone,
                      address=address,
                      rating=rating,
                      review_count=review_count)
        db.session.add(venue)
        db.session.commit()

    check_fav=crud.check_if_fav_exists(user_id, venue.id)

    if check_fav:
        return jsonify({'success': False, 'message': 'Already a favorite'}) 
    else:
        favorite = crud.save_as_favorite(user=user, venue=venue)
        db.session.add(favorite)
        db.session.commit()
        return jsonify({'success': True, 'message': 'Added to favorites!'})
    

@app.route("/logout")
def logout():
    """User logout."""

    session.pop("user_email", None)

    flash("You have been logged out.")
    return redirect("/")


@app.route('/venue_without_fav/<id>')
def get_venue_details_without_fav(id):
    """View the details of a venue."""

    if 'user_email' not in session:
        flash('You need to log in to view venue details.')
        return redirect('/')

    url = f'https://api.yelp.com/v3/businesses/{id}'
    headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
    payload = {'apikey': YELP_API_KEY}

    user_email = session['user_email']
    user_by_email = crud.get_user_by_email(user_email)
    response = requests.get(url, params=payload, headers=headers).json()
    return render_template('venue-details-without-favorite-button.html',
                            business=response,
                            user=user_by_email)


@app.route('/remove-favorite', methods=['POST'])
def remove_favorite():
    """Remove a venue from user's favorites."""
    if 'user_email' not in session:
        return jsonify({'success': False, 'message': 'Please log in to remove a favorite'})

    user = crud.get_user_by_email(session['user_email'])
    if not user:
        return jsonify({'success': False, 'message': 'Please log in to remove a favorite'})

    data = request.json
    external_id = data.get('external_id')
    venue_name = data.get('venue_name')
    phone = data.get('phone')
    address = data.get('address')
    rating = data.get('rating')
    review_count = data.get('review_count')

    venue = crud.get_venue_by_external_id(external_id)
    favorite = crud.get_favorite_by_user_and_venue(user, venue)
    print(favorite)
    db.session.delete(favorite)
    db.session.commit()

    return jsonify({'success': True, 'message': 'Removed from favorites!'})



@app.route('/resources')
def resources():
    """Additional Hawaii resources"""
    if 'user_email' not in session:
        flash('You need to log in to view resources.')
        return redirect('/')

    return render_template('resources.html')



if __name__ == "__main__":
    connect_to_db(app)
    print("http://localhost:5000/")
    app.run(host="0.0.0.0", debug=True)