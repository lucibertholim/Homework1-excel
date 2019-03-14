// Create a map object
var myMap = L.map("map", {
  center: [15.5994, -28.6731],
  zoom: 2.5
});

L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
  attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
  maxZoom: 18,
  id: "mapbox.streets-basic",
  accessToken: API_KEY
}).addTo(myMap);

// Country data
var link = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/2.5_day.geojson"

function getColor(d) {
  if (d >= 5.0)
    return "#FF0000";
  if (d >= 4.0)
    return "#FF6600";
  if (d >= 3.0)
    return "#FF9900";
  if (d >= 2.0)
    return "#FFFF33";
  else
    return "#99FF66";
};


d3.json(link, function(data) {
  L.geoJSON(data, {
    pointToLayer: function (feature, latlng) {
        return L.circleMarker(latlng, {
          radius: feature.properties.mag*2,
          fillColor: getColor(feature.properties.mag),
          color: "#000",
          weight: 0.5,
          opacity: 1,
          fillOpacity: 0.6
        });
    },
    onEachFeature: function (feature, layer) {
      layer.bindPopup('<h4>'+feature.properties.place+'</h4><p>Magnitude: '+feature.properties.mag+'</p>');
    }
  }).addTo(myMap);



});
