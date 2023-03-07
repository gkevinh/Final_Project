function initMap() {
    const directionsRenderer = new google.maps.DirectionsRenderer();
    const directionsService = new google.maps.DirectionsService();
    const map = new google.maps.Map(document.querySelector("#map"), {
        zoom: 14,
        center: {lat:21.3099, lng: -157.8581},
    })

    directionsRenderer.setMap(map);
    calculateAndDisplayRoute(directionsService, directionsRenderer);
    document.getElementById("mode").addEventListener("change", () => {
        calculateAndDisplayRoute(directionsService,directionsRenderer);
    })
}

function calculateAndDisplayRoute(directionsService, directionsRenderer){
    const selectedMode=document.querySelector("#mode").value;

    directionsService
    .route({
        origin: document.querySelector("#from").value,
        destination: document.querySelector("#to").value,

        travelMode: google.maps.TravelMode[selectedMode],


    })
    .then((response) => {
        directionsRenderer.setDirections(response);
    })
    .catch((e)=> alert("Direction request failed"));

}

function initMap(){}