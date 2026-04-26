// Store API endpoint inside queryUrl
var queryUrl = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"


// Perform a get request to the query URL
d3.json(queryUrl).then(function(data){
    // Once we get a response, send the data.features object to the createFeatures function
    createFeatures(data.features);
    console.log(data);
})

//
function createFeatures(earthquakeData) {

    // Define a function we want to run once for each feature in the features array
    // Give each feature a popup describing the place,time, and the magnitude of the earthquake
    function onEachFeature(feature, layer) {
        layer.bindPopup("<h3>" + feature.properties.place +
      "</h3><hr><p>" + new Date(feature.properties.time) + "</p>" +
      "</h3><hr><p>" + "Magnitude: "+feature.properties.mag + "</p>");
    }

    // Create circlemarkers on the geoJson layer
    function geojsonMarkerOptions(feature) {
        return {

        radius: feature.properties.mag*5,
        fillColor: getColor(feature.properties.mag),
        color: "#000",
        weight: 1,
        opacity: 1,
        stroke: true,
        fillOpacity: 1
        }
    };
    // // function change color of the circle based on magnitude
    // function color(magnitude) {
    //     if (magnitude <= 1) {
    //     return "#B7F34D";
    //     } else if (magnitude <= 2) {
    //     return "#E1F34D";
    //     } else if (magnitude <= 3) {
    //     return "#F3DB4D";
    //     } else if (magnitude <= 4) {
    //     return "#F3BA4D";
    //     } else if (magnitude <= 5) {
    //     return "#F0A76B";
    //     } else {
    //     return "#F06B6B";
    //     }

    // }

    // Create a GeoJSON layer containing the features array on the earthquakeData object
    // Run the onEachFeature function once for each piece of data in the array
    var earthquakes=L.geoJSON(earthquakeData, {
        pointToLayer: function (feature, latlng) {
            return L.circleMarker(latlng, geojsonMarkerOptions(feature))},
        onEachFeature: onEachFeature
    });

    createMap(earthquakes);
}

// function to change circle color based on earthquake magitude
function getColor(magnitude) {
    return magnitude > 5 ? "#F06B6B" :
           magnitude > 4 ? "#F0A76B" :
           magnitude > 3 ? "#F3BA4D" :
           magnitude > 2 ? "#F3DB4D" :
           magnitude > 1 ? "#E1F34D" :
                           "#B7F34D"; 
  }
  

function createMap(earthquakes) {

    //Define lightmap layers
    var lightmap=L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
      attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
      maxZoom: 18,
      id: "mapbox.light",
      accessToken: API_KEY
    })

    // var baseMaps = {
    //     "Light Map": lightmap,
    //   };
    // var overlayMaps = {
    //     Earthquakes: earthquakes
    //   };
    
    // Create map, giving it the streetmap and earthquakes layers to display on load
    var map = L.map("map", {
        center: [39.09, -95.71],
        zoom: 6,
        layers: [lightmap,earthquakes]
    });
    
    // add legend
    var legend = L.control({position: 'bottomright'});
      
    legend.onAdd = function (map) {

        var div = L.DomUtil.create('div', 'info legend'),
        grades = [0, 1, 2, 3, 4, 5],
        labels = [];

    // loop through our density intervals and generate a label with a colored square for each interval
        for (var i = 0; i < grades.length; i++) {
            div.innerHTML +=
                '<i style="background:' + getColor(grades[i] + 1) + '"></i> ' +
                grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
                console.log(getColor(grades[i]+1));
        }

    
        return div;
    };

    legend.addTo(map);
    
}
