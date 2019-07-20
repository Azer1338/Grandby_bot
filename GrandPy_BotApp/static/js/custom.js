// Message
console.log("Custom JQuery loaded");

// Event on click button
$('button').click(function () {
	
	// Message 
	console.log("User click on button");
	
	// Gather the User's sentence
	var userRequest = document.getElementById("User_destination");
	
	$.ajax({
		// Route to /result/ page in views.py
        url: '/result/',
        // Data to send
        data: {query : userRequest.value},
        // Return accepted format
        dataType: 'json',
        
        // In case of succes - json_data is return from AJAX GET call
        success: function(json_data) {
			// Message
            console.log(json_data);

			// Generate a map through Google Map
			initMap(json_data.lat,json_data.lng, 'googleMap')
			},
			
		// In case of error
        error : function(resultat, statut, erreur){
			// Message
			console.log("AJAX (Get) function turn crazy");
			}
		});
	});


// Google Map integration in the website
function initMap(latitude, longitude, IdHTML ) {

	// Grab the right id element in the HTML
	var mapElement = document.getElementById(IdHTML);
	
	// Creation of the map element
	map_ref = new google.maps.Map(mapElement, {
		center: {lat: latitude, lng: longitude},
		zoom: 18
		});
}
