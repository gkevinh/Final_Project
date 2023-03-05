import os, requests
from pprint import pprint
import json

YELP_API_KEY = os.environ['YELP_KEY']

def call_yelp_api():
    """Search for venues"""

    endpoint = "https://api.yelp.com/v3/businesses/search"
    headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
    payload = {'limit' : '15', 'location' : '96815', 'categories' : 'desserts'}

    response = requests.get(endpoint, params=payload, headers=headers).json()

    pprint(response['businesses'])

    # business_data = response.json()

    # print(json.dumps(business_data, indent = 3))

call_yelp_api()