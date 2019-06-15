
console.log("JQuery loaded");

// Initiatialisation of the tchat area 
var tchatList = [
    {
        from: "GrandPy",
        kind_of: "text",
        content: "Ou veux tu aller mon pitchoune?"
    },
    {
        from: "User",
        kind_of: "form",
        content: "Tape ton adresse ici!"
    },
/*
    {
        from: GrandPy,
        kind_of: API_answer,
        content: Google_Maps
    },
        {
        from: GrandPy,
        kind_of: API_answer,
        content: MediaWiki
    },
 */
];

// Create and display a DOM elment in the thcat area
function createElementDiscussion(bubble) {
	
	var contentElt = document.createElement("div");
	
	// Display
	switch (bubble.from) {
		case "GrandPy":
			contentElt.setAttribute("class","row bubble bubble_right");
			break;
		case "User":
			contentElt.setAttribute("class","row bubble bubble_left");
			break;
		default:
			console.log("Element built not known - Display");
	}
	
	// Content
	switch (bubble.kind_of) {
		case "text":
			// Text area
			var textElt = document.createElement("p");
			textElt.textContent = bubble.content;
			contentElt.appendChild(textElt);
			break;
		case "form":
			// Input
			var inputElt = document.createElement("input");
			inputElt.id = "User_destination";
			inputElt.setAttribute("placeholder",bubble.content);
			inputElt.setAttribute("maxlength","30");
			contentElt.appendChild(inputElt);
			
			//Button
			var ButtonElt = document.createElement("button");
			ButtonElt.id = "Destination_btn";
			ButtonElt.setAttribute("class","btn btn-primary");
			ButtonElt.setAttribute("type","button");
			ButtonElt.setAttribute("required", "true");
			ButtonElt.appendChild(document.createTextNode("Envoi"));
			contentElt.appendChild(ButtonElt);
			break;
		default:
			console.log("Element built not known - Content");
	}

    return contentElt;
}

// Display the Tchat content
// Find and secure the right container
var contenuElt = document.getElementById("Tchat");
// Display discussion element from list
tchatList.forEach(function(bubble){
	//Element creation
	var tchatElt = createElementDiscussion(bubble);
	//Add element
	contenuElt.appendChild(tchatElt);
	});

// Create and send a request

$('button').click(function () {
    console.log("Button Clicked");

	var userRequest = document.getElementById("User_destination");
	
	// Gather the User's request
	var tchat = {
            from: "GrandPy",
            kind_of: "text",
            content: "Oh... Je connais bien "+userRequest.value
        };

	// Display in console the value
	console.log(userRequest.value);
	
	// Display User's request
	var tchatElt = createElementDiscussion(tchat);
	contenuElt.appendChild(tchatElt);
        
});
