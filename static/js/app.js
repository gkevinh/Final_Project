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

function failure(){}