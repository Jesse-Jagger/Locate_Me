let map;

function initMap() {
    map = new google.maps.Map(document.getElementById('map'), {
        center: { lat: -34.397, lng: 150.644 },
        zoom: 8
    });

    fetchMarkers();
}

async function fetchMarkers() {
    const response = await fetch('/api/map/markers');
    const markers = await response.json();

    markers.forEach(marker => {
        new google.maps.Marker({
            position: { lat: marker.lat, lng: marker.lng },
            map: map,
            title: marker.title
        });
    });
}

// Load the Google Maps API asynchronously
function loadGoogleMaps() {
    var script = document.createElement('script');
    script.src = 'https://maps.googleapis.com/maps/api/js?key=AIzaSyD8wpWOJOtJy1KVdiihGcXHlHLVJchcicc&callback=initMap';
    script.defer = true;
    script.async = true;
    document.body.appendChild(script);
}

// Call the function to load the Google Maps API
loadGoogleMaps();