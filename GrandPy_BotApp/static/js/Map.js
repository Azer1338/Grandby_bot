

// Console print of the query
console.log("googleMapsAPI: " + {{ place_requested }});

// Record the query
var address = {{ place_requested }};

// Initialisation of the map
var latlng = new google.maps.LatLng(0, 0);
var mapOptions = 	{	zoom: 14,
						center: latlng
					}

// Map creation
var map = new google.maps.Map(document.getElementById('map'),mapOptions);
var geocoder = new google.maps.Geocoder();

geocoder.geocode( { 'address': address}, function(results, status) {
	if (status == 'OK') {
		map.setCenter(results[0].geometry.location);
		
		var marker = new google.maps.Marker({
			map: map,
			position: results[0].geometry.location
		});
	} 	
	else {
		alert('Geocode was not successful for the following reason: ' + status);
	}
	});
	
// Push in the screen
document.getElementById("GrandPyAnswer").innerHTML = map;
