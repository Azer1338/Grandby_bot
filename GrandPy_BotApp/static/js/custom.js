
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
	
	// Loading picture
	loadingPicture("on","Input_bar");
	
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
			var request = document.createElement("p");
			request.textContent = userRequest.value;
			displayElement("User", request);
			
			// Display GrandPy's answer			
			var answer = document.createElement("p");
			answer.textContent = randomGrandPyAnswer() + " " + json_data.about;			
			displayElement("GrandPy",answer);
			
			// Generate a map through Google Map and display it
			generateMap(json_data.lat,json_data.lng, 'googleMap');
			
			// Retry?
			var enough = document.createElement("p");
			enough.textContent = "Autre part?";
			displayElement("GrandPy",enough);
			
			// Initialise the user field
			initField();
			
			// Unloading picture
			loadingPicture("off","Input_bar");
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
function displayElement (fromWho, elt){
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
	
	// Push the element in the bubble
	containerElt.appendChild(elt);

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
};

// Init user's field
function initField(){

	// Replace the filed by a blank area
	var user = document.getElementById("User_destination");
	
	user.value = "";
};

// Manage the loading picture
function loadingPicture (status,element){

	switch (status) {
		case "on":
			// Message
			console.log("loading pic on");
			
			// Add a bubble
			var pic = document.createElement("img");
			
			// Modify attributs
			pic.setAttribute("src","/static/img/loading.gif");
			pic.id = "loading";
			
			// Place the image in the screen
			var elt = document.getElementById(element);
			
			displayElement("GrandPy",pic);
			break;
			
		case "off":
			// Message
			console.log("loading pic off");
			
			// Remove the bubble
			var elt = document.getElementById(element);
			
			elt.replaceChild(elt.childNodes[2]);
			
			break;
	};

};	
