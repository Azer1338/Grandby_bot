
// Event on keyboard pressed
$( "#User_destination" ).keypress(function( event ) {
  // Enter key pressed
  if ( event.which == 13 ) {
     
     // Message
     console.log('User type on Enter key');
     
     userMessageSending();
  }
});

// Event on click button
$('button').click(function () {
	
	// Message 
	console.log("User click on button");
	
     userMessageSending();
});

// Actions following User's message sending to the website
function userMessageSending(){
	// Gather the User's sentence
	var userRequest = document.getElementById("User_destination");
	
	// Call to views.py
	$.ajax({
		// Route to /result/ page in views.py
        url: '/result/',
        // Data to send with
        data: {query : userRequest.value},
        // Return accepted format
        dataType: 'json',
        
        // In case of succes - json_data will be returned from AJAX GET call
        success: function(json_data) {
			// Message
            console.log(json_data);

			// Generate a map through Google Map
			generateMap(json_data.lat,json_data.lng, 'googleMap');
			
			// Generation of the what-about text
			generateText(json_data.about, 'mediaWiki');
			
			},
			
		// In case of error
        error: function(result, status, error_type){
			// Message
			console.log("AJAX (Get) function turn crazy " + error_type);
		}
	});
};

// Google Map integration in the website
function generateMap(latitude, longitude, IdHTML ) {
// Generate a Google map from :latitude & :longitude
// Element will be pinned to the :IdHTML

	// Grab the right id element in the HTML
	var mapElement = document.getElementById(IdHTML);
	
	// Creation of the map element
	map_ref = new google.maps.Map(mapElement, {
		center: {lat: latitude, lng: longitude},
		zoom: 18
		});
}

function generateText(textToDisplay, IdHTML){
// Generate a text from :textToDisplay
// Element will be pinned to the :IdHTML

	// Load GrandPy's answers
	GrandPy = $.ajax({
		url:"GrandPy_answer.json",
		sucess: function(json_file){
			console.log(json_file);
		},
		// In case of error
        error: function(result, status, error_type){
			// Message
			console.log("AJAX (Get) function turn crazy " + error_type);
		}
	});
	
	// Grab the right id element in the HTML and modify text
	document.getElementById(IdHTML).innerHTML = "Sais-tu que ... " + textToDisplay; 
}
