
// Event on keyboard pressed
$( "#User_destination" ).keypress(function( event ) {
  // Enter key pressed
  if ( event.which == 13 ) {
     
     // Message
     console.log('User type on Enter key');
     
     // Manage the interface
     interfaceManagement();
  }
});

// Actions following User's message sending to the website
function interfaceManagement(){
// Manage the UI

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
			
			// Display User's request
			displayElement("User",userRequest.value);
			
			// Display GrandPy's answer			
			var grandPyAnswer = randomGrandPyAnswer() + " " + json_data.about;			
			displayElement("GrandPy",grandPyAnswer);
			
			// Generate a map through Google Map and display it
			generateMap(json_data.lat,json_data.lng, 'googleMap');
			
			// Retry?
			displayElement("GrandPy","Autre part?");
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

// Display a message in the Tchat aera
function displayElement (fromWho, texte){
// Display an :element on interface with :fromWho 's design
	
	// Container creation
	var containerElt = document.createElement("div");
	switch (fromWho){
		case "GrandPy":
			containerElt.setAttribute("class","row bubble_right bubble right");
			break;
		case "User":
			containerElt.setAttribute("class","row bubble_left bubble left");
			break;
		default:
			console.log("containerElt not defined");
	}
	
	// Content creation
	var content = document.createElement("p");
	content.textContent = texte;
	containerElt.appendChild(content);

	// Add a bubble in the tchat area
	var textArea = document.getElementById("Tchat");
	textArea.insertAdjacentElement("beforeend",containerElt);
};

// GrandPy's answer integration in the website
function randomGrandPyAnswer(){
// Generate a random text from JSON file.

	// GrandPy introduction
	var randomAnswer = "Sais-tu que ... ";
	
	// Load GrandPy's answers
	$.getJSON(
		"/static/json/GrandPy_answer.json",
		function(json_file){
			console.log("sucess - randomGrandPyAnswer");
			console.log(json_file);
			
			// Define a random number included in the json file length
			var randomNumber = Math.floor(Math.random()* json_file.Beginning.length);
			
			// Message
			console.log("#: " + randomNumber + "|txt: " + json_file.Beginning[randomNumber]);
			
			// Grab the right id element in the HTML and modify text
			randomAnswer = json_file.Beginning[randomNumber];
	});
	console.log("GdPy answwer " + randomAnswer);
	
	// Return a string
	return randomAnswer;
}

