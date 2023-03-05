// import os, requests
// from pprint import pprint
// import json

GOOGLE_API_KEY = os.environ['GOOGLE_KEY']

// def call_yelp_api():
//     """Search for venues"""

//     endpoint = "https://api.yelp.com/v3/businesses/search"
//     headers = {'Authorization': 'Bearer %s' % YELP_API_KEY}
//     payload = {'limit' : '30', 'location' : '90404', 'categories' : 'desserts'}

//     response = requests.get(endpoint, params=payload, headers=headers).json()

//     pprint(response['businesses'])

//     # business_data = response.json()

//     # print(json.dumps(business_data, indent = 3))


// call_yelp_api()




function initMap() {
    const locations = [
      {
        name: 'Hackbright Academy',
        coords: {
          lat: 37.7887459,
          lng: -122.4115852,
        },
      },
      {
        name: 'Powell Street Station',
        coords: {
          lat: 37.7844605,
          lng: -122.4079702,
        },
      },
      {
        name: 'Montgomery Station',
        coords: {
          lat: 37.7894094,
          lng: -122.4013037,
        },
      },
    ];
  
    const markers = [];
    for (const location of locations) {
      markers.push(
        new google.maps.Marker({
          position: location.coords,
          title: location.name,
          map: basicMap,
          icon: {
            // custom icon
            url: '/static/img/marker.svg',
            scaledSize: {
              width: 30,
              height: 30,
            },
          },
        }),
      );
    }
  
    for (const marker of markers) {
      const markerInfo = `
        <h1>${marker.title}</h1>
        <p>
          Located at: <code>${marker.position.lat()}</code>,
          <code>${marker.position.lng()}</code>
        </p>
      `;
  
      const infoWindow = new google.maps.InfoWindow({
        content: markerInfo,
        maxWidth: 200,
      });
  
      marker.addListener('click', () => {
        infoWindow.open(basicMap, marker);
      });
    }
  }