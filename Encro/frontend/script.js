let map;
let infoWindow;

function initMap() {

map = new google.maps.Map(

document.getElementById("map"),

{
center: { lat: 24.5968, lng: 76.1647 },
zoom: 11
}

);

infoWindow = new google.maps.InfoWindow();

map.data.loadGeoJson("/encro/jhalawar.geojson");

map.data.setStyle({

fillColor: "#6a1b9a",
strokeColor: "#4a148c",
strokeWeight: 2,
fillOpacity: 0.4

});


map.data.addListener("click", function (event) {

const geometry = event.feature
.getGeometry()
.getArray()[0]
.getArray();

let coords = geometry.map(coord => [

coord.lng(),
coord.lat()

]);

coords.push(coords[0]);

sendToBackend(coords, event.latLng);

});

}



function sendToBackend(coords, clickLatLng) {

fetch(

"/analyze",

{

method: "POST",

headers: {

"Content-Type": "application/json"

},

body: JSON.stringify({

coordinates: [coords]

})

}

)

.then(response => response.json())

.then(data => {

console.log(data);


// Update sidebar

document.getElementById("forest").innerText =
data.forest_percent + "%";

document.getElementById("agriculture").innerText =
data.agriculture_percent + "%";

document.getElementById("other").innerText =
data.other_percent + "%";


// Show popup on map ONLY

infoWindow.setContent(

"<b>Land Cover Analysis</b><br>" +
"Forest: " + data.forest_percent + "%<br>" +
"Agriculture: " + data.agriculture_percent + "%<br>" +
"Other: " + data.other_percent + "%"

);

infoWindow.setPosition(clickLatLng);

infoWindow.open(map);

});

}