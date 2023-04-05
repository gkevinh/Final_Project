let map, directionsService, directionsRenderer;

function initMap() {
    // Initialize the map and directions service
    const mapOptions = {
        zoom: 10,
        mapTypeId: google.maps.MapTypeId.ROADMAP
    }
    map = new google.maps.Map(document.querySelector("#map"), mapOptions);

    directionsService = new google.maps.DirectionsService();
    directionsRenderer = new google.maps.DirectionsRenderer({
        map: map,
        panel: document.getElementById("directions-panel"),
    });

    // Get the user's location and set it as the center of the map
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition((position) => {
            const myLat = position.coords.latitude;
            const myLong = position.coords.longitude;
            const coords = new google.maps.LatLng(myLat, myLong);
            map.setCenter(coords);

            const latitude = document.getElementById("lat").value * 1;
            const longitude = document.getElementById("long").value * 1;

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
                    displayDirections(response);
                } else {
                    // alert(`Directions request unsuccessful due to: ${status}`);
                    swal("Directions request unsuccessful");
                }
            });
        }, () => {
            // alert("Failed to get the user's location");
            swal("Failed to get the user's location");
        });
    } else {
        // alert("Geolocation is not supported by this browser.");
        swal("Geolocation is not supported by this browser");
    }
}

// function displayDirections(response) {
//     const directions = response.routes[0].legs[0].steps;
//     const directionsPanel = document.getElementById('directions-panel');
//     let html = '<ol>';

//     for (let i = 0; i < directions.length; i++) {
//         html += '<li>' + directions[i].instructions + '</li>';
//     }

//     html += '</ol>';
//     directionsPanel.innerHTML = html;
// }

const x = navigator.geolocation;
x.getCurrentPosition(success, failure);
