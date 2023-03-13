x=navigator.geolocation

x.getCurrentPosition(success, failure);

const latitude = document.getElementById("lat").value * 1;
const longitude = document.getElementById("long").value * 1;


function success(position) {
    let myLat = position.coords.latitude;
    let myLong = position.coords.longitude;
    
    let coords = new google.maps.LatLng(myLat, myLong);

    console.log(coords)

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

    const directionsService = new google.maps.DirectionsService();


    const directionsRenderer = new google.maps.DirectionsRenderer();
    directionsRenderer.setMap(map);

    const hbToPowellRoute = {
        origin: {
        lat: myLat,
        lng: myLong,
        },
        destination: {
        lat: latitude,
        lng: longitude,
        },
        travelMode: 'DRIVING',
    };

    directionsService.route(hbToPowellRoute, (response, status) => {
        if (status === 'OK') {
        directionsRenderer.setDirections(response);
        } else {
        alert(`Directions request unsuccessful due to: ${status}`);
        }
    });
    directionsRenderer.setMap(map);
    directionsRenderer.setPanel(document.getElementById("sidebar"));

    const control = document.getElementById("floating-panel");

    map.controls[google.maps.ControlPosition.TOP_CENTER].push(control);

    const onChangeHandler = function () {
        calculateAndDisplayRoute(directionsService, directionsRenderer);
    };

    document.getElementById("start").addEventListener("change", onChangeHandler);
    document.getElementById("end").addEventListener("change", onChangeHandler);

    function calculateAndDisplayRoute(directionsService, directionsRenderer) {
        const start = document.getElementById("origin").value;
        const end = document.getElementById("destination").value;
      
        directionsService
          .route({
            origin: start,
            destination: end,
            travelMode: google.maps.TravelMode.DRIVING,
          })
          .then((response) => {
            directionsRenderer.setDirections(response);
          })
          .catch((e) => window.alert("Directions request failed due to " + status));
      }
}

function initMap(){}
function failure(){}
