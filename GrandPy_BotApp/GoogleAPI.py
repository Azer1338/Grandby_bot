#KEY
googleMapsKey = "AIzaSyBdRHj_DnOYzEHO5oa0RMIWu0Wp9hrKSnY";

#Google Maps API
function googleMapsAPI(placeTodisplay){
	console.log("googleMapsAPI: " + placeTodisplay);
	
	// Add a bubble
	var tchat = {
		from: "GrandPy",
        kind_of: "Google_Maps_answer",
        content: "Google_Maps"
	};
	
	// Display User's request
	var tchatElt = createElementDiscussion(tchat);
	contenuElt.appendChild(tchatElt);
	
	//
	var address = placeTodisplay;
	var latlng = new google.maps.LatLng(0, 0);
	var mapOptions = {
		zoom: 14,
		center: latlng
		}
	var map = new google.maps.Map(document.getElementById('map'),mapOptions);
	var geocoder = new google.maps.Geocoder();

	geocoder.geocode( { 'address': address}, function(results, status) {
		if (status == 'OK') {
			map.setCenter(results[0].geometry.location);
			var marker = new google.maps.Marker({
			map: map,
			position: results[0].geometry.location
			});
		} else {
			alert('Geocode was not successful for the following reason: ' + status);
		}
	});
};
