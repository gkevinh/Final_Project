
  document.querySelector('#display-directions').addEventListener('click', () => {
    const directionsService = new google.maps.DirectionsService();

    // The DirectionsRenderer object is in charge of drawing directions
    // on maps
    const directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);

    const directions = {
      origin: {
        lat: 37.7887459,
        lng: -122.4115852,
      },
      destination: {
        lat: 37.7844605,
        lng: -122.4079702,
      },
      travelMode: 'DRIVING',
    };

    directionsService.route(directions, (response, status) => {
      if (status === 'OK') {
        directionsRenderer.setDirections(response);
      } else {
        alert(`Directions request unsuccessful due to: ${status}`);
      }
    });
  });



  function initMap() {
    var pointA = new google.maps.LatLng(51.7519, -1.2578),
      pointB = new google.maps.LatLng(50.8429, -0.1313),
      myOptions = {
        zoom: 7,
        center: pointA
      },
      map = new google.maps.Map(document.getElementById('map-canvas'), myOptions),
      // Instantiate a directions service.
      directionsService = new google.maps.DirectionsService,
      directionsDisplay = new google.maps.DirectionsRenderer({
        map: map
      }),
      markerA = new google.maps.Marker({
        position: pointA,
        title: "point A",
        label: "A",
        map: map
      }),
      markerB = new google.maps.Marker({
        position: pointB,
        title: "point B",
        label: "B",
        map: map
      });
  
    // get route from A to B
    calculateAndDisplayRoute(directionsService, directionsDisplay, pointA, pointB);
  
  }
  
  
  
  function calculateAndDisplayRoute(directionsService, directionsDisplay, pointA, pointB) {
    directionsService.route({
      origin: pointA,
      destination: pointB,
      travelMode: google.maps.TravelMode.DRIVING
    }, function(response, status) {
      if (status == google.maps.DirectionsStatus.OK) {
        directionsDisplay.setDirections(response);
      } else {
        window.alert('Directions request failed due to ' + status);
      }
    });
  }
  
  initMap();



  x=navigator.geolocation

x.getCurrentPosition(success, failure);

function success(position) {
    let myLat = position.coords.latitude;
    let myLong = position.coords.longitude;

    let coords = new google.maps.LatLng(myLat, myLong);

    let mapOptions = {
        zoom: 10,
        center: coords,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    let map = new google.maps.Map(document.querySelector("#map"), mapOptions);

    let marker = new google.maps.Marker({
        map:map,
        position: coords
    });

}

function initMap(){}
function failure(){}