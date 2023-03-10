// x=navigator.geolocation

// x.getCurrentPosition(success, failure);

// const latitude = document.getElementById("lat").value * 1;
// const longitude = document.getElementById("long").value * 1;


// function success(position) {
//     let myLat = position.coords.latitude;
//     let myLong = position.coords.longitude;
    
//     let coords = new google.maps.LatLng(myLat, myLong);

//     console.log(coords)

//     let mapOptions = {
//         zoom: 10,
//         center: coords,
//         mapTypeId: google.maps.MapTypeId.ROADMAP
//     }
//     let map = new google.maps.Map(document.querySelector("#map"), mapOptions);

//     let marker = new google.maps.Marker({
//         map:map,
//         position: coords
//     });

//     const directionsService = new google.maps.DirectionsService();


//     const directionsRenderer = new google.maps.DirectionsRenderer();
//     directionsRenderer.setMap(map);

//     const hbToPowellRoute = {
//         origin: {
//         lat: myLat,
//         lng: myLong,
//         },
//         destination: {
//         lat: latitude,
//         lng: longitude,
//         },
//         travelMode: 'DRIVING',
//     };

//     directionsService.route(hbToPowellRoute, (response, status) => {
//         if (status === 'OK') {
//         directionsRenderer.setDirections(response);
//         } else {
//         alert(`Directions request unsuccessful due to: ${status}`);
//         }
//     });
// }

// function initMap(){}
// function failure(){}







x=navigator.geolocation

x.getCurrentPosition(success, failure);

const latitude = document.getElementById("lat").value * 1;
const longitude = document.getElementById("long").value * 1;

function success(position) {

    const myLat = position.coords.latitude;
    const myLong = position.coords.longitude;
    
    const coords = new google.maps.LatLng(myLat, myLong);

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

    const start = new google.maps.LatLng(myLat, myLong);
    const end = new google.maps.LatLng(latitude, longitude);

    directionsRenderer.setMap(map);
    directionsRenderer.setPanel(document.getElementById("sidebar"));

    const control = document.getElementById("floating-panel");

    map.controls[google.maps.ControlPosition.TOP_CENTER].push(control);

    const onChangeHandler = function () {
        calculateAndDisplayRoute(directionsService, directionsRenderer);
    };


    function calculateAndDisplayRoute(directionsService, directionsRenderer) {
        const start = document.getElementById("start").value;
        const end = document.getElementById("end").value;
      
        directionsService
          .route({
            origin: start,
            destination: end,
            travelMode: google.maps.TravelMode.DRIVING,
          })
          .then((response) => {
            directionsRenderer.setDirections(response);
          })
          .catch((e) => window.alert("Directions request failed"));
    }
}

function initMap(){}
function failure(){}