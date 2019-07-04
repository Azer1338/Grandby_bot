// Reaching console log
console.log("JQuery loaded");

// Init the tchat area 
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
    }
];

// Create DOM elment in the tchat area
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
			inputElt.setAttribute("maxlength","45");
			contentElt.appendChild(inputElt);
			
			// Button
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

// Create DOM elment in the tchat area
var contenuElt = document.getElementById("Tchat");

tchatList.forEach(function(bubble){
	//Element creation
	var tchatElt = createElementDiscussion(bubble);
	//Add element
	contenuElt.appendChild(tchatElt);
	});

// Event on click button
$('button').click(function () {
    
	var userRequest = document.getElementById("User_destination");
	
	console.log("la localisation choisie est: " + userRequest.value);
	
	var user1 = 'Adrien';
	var user2 = 'Gael';

	$.get({
        url: '/result/',
        //A renvoyer a la vue
        data: { student : user1, teacher : user2, place : userRequest.value},
        success: function(data) {
            console.log(data);
            
        var usRequest = document.getElementById("GrandPyAnswer");
        usRequest.innerHTML = data;    
        }
    });
    
	console.log("Button Clicked");
});
