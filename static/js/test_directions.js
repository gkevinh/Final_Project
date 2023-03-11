'use strict';

document.querySelector('#display-directions').addEventListener('click', () => {
  const directionsService = new google.maps.DirectionsService();

  // The DirectionsRenderer object is in charge of drawing directions
  // on maps
  const directionsRenderer = new google.maps.DirectionsRenderer();
  directionsRenderer.setMap(map);

  const hbToPowellRoute = {
    origin: {
      lat: 37.7887459,
      lng: -122.4115852,
    },
    destination: {
      lat: 37.7844605,
      lng: -122.4079702,
    },
    travelMode: 'WALKING',
  };

  directionsService.route(hbToPowellRoute, (response, status) => {
    if (status === 'OK') {
      directionsRenderer.setDirections(response);
    } else {
      alert(`Directions request unsuccessful due to: ${status}`);
    }
  });
});
}