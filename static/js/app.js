x=navigator.geolocation

x.getCurrentPosition(success, failure);

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
        lat: 34.1122,
        lng: -118.3391,
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

}

function initMap(){}
function failure(){}
