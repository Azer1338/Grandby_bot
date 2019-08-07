// Event on keyboard pressed
$( "#User_destination" ).keypress(function( event ) {
  // "ENTER" key pressed
  if ( event.which == 13 ) {
     
     // Message
     console.log('User type on Enter key');
     
     // Call APIs, display elements to website
     processingUserRequest();
  }
});

// Actions following User's message sending to the website
function processingUserRequest(){
// Manage the UI

	// Gather the User's sentence
	var userRequest = document.getElementById("User_destination");
	
	// Show a loading picture
	var pic = loadingPicture("on","Input_bar");
	displayElement("GrandPy",pic);
	
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
			var request = generateTexte(userRequest.value);
			displayElement("User", request);
			
			// Display GrandPy's answer
			var answerAbout = generateTexte(json_data.sentence + " " + json_data.about);			
			displayElement("GrandPy",answerAbout);
			
			// Display GrandPy's map
			var answerMap = generateMap (json_data.lat,json_data.lng);
			displayElement("GrandPy",answerMap);
			
			// Retry?
			var answerEnough = generateTexte("Autre part?");
			displayElement("GrandPy",answerEnough);
			
			// Initialise the user field
			cleanInputForm();
			
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
function generateMap(latitude, longitude) {
// Generate a Google map from :latitude & :longitude
// Element will be pinned to the :IdHTML

	// Create an element as container
	var mapElement = document.createElement("div");
	mapElement.setAttribute("id","googleMap");
	
	// Creation of the map element
	map_ref = new google.maps.Map(mapElement, {
		center: {lat: latitude, lng: longitude},
		zoom: 14
		});

	return mapElement;
}

// Return a <p> element
function generateTexte (text){

	// Generate a <p> element
	var textElt = document.createElement("p");
	textElt.textContent = text;

	return textElt;
};

// Return a <img> element
function generateImage(source){

		// Generate a <p> element
		var picture = document.createElement("img");
		picture.setAttribute("src",source);
		picture.setAttribute("class","generateImg");
			
		return picture;
};

// Display a message in the Tchat aera
function displayElement (fromWho, elt){
// Display an :element on interface with :fromWho 's design
	
	// Container creation
	var containerElt = document.createElement("div");
	var containerPicture = document.createElement("div");
	var picture;
	
	// Depending on who is talking
	switch (fromWho){
		case "GrandPy":
			containerElt.setAttribute("class","row bubble_right bubble right");
			picture = generateImage("/static/img/GrandPy_Logo.png");
			
			// Fill the container with elt and picture
			containerElt.appendChild(elt);
			
			containerPicture.appendChild(picture);
			containerElt.appendChild(containerPicture);
			break;
			
		case "User":
			containerElt.setAttribute("class","row bubble_left bubble left");
			picture = generateImage("/static/img/Bebe_Logo.png");
			
			// Fill the container with elt and picture
			containerPicture.appendChild(picture);
			containerElt.appendChild(containerPicture);
			
			containerElt.appendChild(elt);
			break;
			
		default:
			console.log("displayElement : containerElt not defined");
	}
	
	// Picture & element position
	containerPicture.setAttribute("class","col-md-4");
	elt.setAttribute("class","col-md-8");	

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
function cleanInputForm(){

	// Replace the filed by a blank area
	var user = document.getElementById("User_destination");
	
	user.value = "";
};

// Manage the loading picture
function loadingPicture (status){
	
	// Switch On / Off the picture
	switch (status) {
		case "on":
			// Message
			console.log("loading pic on");
			
			// Add a bubble
			var pic = document.createElement("img");
			
			// Modify attributs
			pic.setAttribute("id","loading");
			pic.setAttribute("src","/static/img/loading.gif");
			
			break;
			
		case "off":
			// Message
			console.log("loading pic off");
			
			// Remove the bubble
			var elt = document.getElementById("loading");
			elt.parentNode.remove();
			
			break;
	};
	
	return pic;
};

// Initialisation
function grandPyIntroduction(){
	
	// Creation of the GrandPy's first sentence
	var init = generateTexte("Bonjour mon pitchoune! Je suis GrandPy Bot, le papi robot! Où veux tu aller?");
	displayElement("GrandPy", init);	
};

// At the website launching
grandPyIntroduction();
