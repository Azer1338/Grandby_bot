// Init
var parseFr = ["a","abord","absolument","afin","ah","ai","aie","ailleurs","ainsi","ait","allaient","allo","allons","allô","alors","anterieur","anterieure","anterieures","apres","après","as","assez","attendu","au","aucun","aucune","aujourd","aujourd'hui","aupres","auquel","aura","auraient","aurait","auront","aussi","autre","autrefois","autrement","autres","autrui","aux","auxquelles","auxquels","avaient","avais","avait","avant","avec","avoir","avons","ayant","b","bah","bas","basee","bat","beau","beaucoup","bien","bigre","boum","bravo","brrr","c","car","ce","ceci","cela","celle","celle-ci","celle-là","celles","celles-ci","celles-là","celui","celui-ci","celui-là","cent","cependant","certain","certaine","certaines","certains","certes","ces","cet","cette","ceux","ceux-ci","ceux-là","chacun","chacune","chaque","cher","chers","chez","chiche","chut","chère","chères","ci","cinq","cinquantaine","cinquante","cinquantième","cinquième","clac","clic","combien","comme","comment","comparable","comparables","compris","concernant","contre","couic","crac","d","da","dans","de","debout","dedans","dehors","deja","delà","depuis","dernier","derniere","derriere","derrière","des","desormais","desquelles","desquels","dessous","dessus","deux","deuxième","deuxièmement","devant","devers","devra","different","differentes","differents","différent","différente","différentes","différents","dire","directe","directement","dit","dite","dits","divers","diverse","diverses","dix","dix-huit","dix-neuf","dix-sept","dixième","doit","doivent","donc","dont","douze","douzième","dring","du","duquel","durant","dès","désormais","e","effet","egale","egalement","egales","eh","elle","elle-même","elles","elles-mêmes","en","encore","enfin","entre","envers","environ","es","est","et","etant","etc","etre","eu","euh","eux","eux-mêmes","exactement","excepté","extenso","exterieur","f","fais","faisaient","faisant","fait","façon","feront","fi","flac","floc","font","g","gens","h","ha","hein","hem","hep","hi","ho","holà","hop","hormis","hors","hou","houp","hue","hui","huit","huitième","hum","hurrah","hé","hélas","i","il","ils","importe","j","je","jusqu","jusque","juste","k","l","la","laisser","laquelle","las","le","lequel","les","lesquelles","lesquels","leur","leurs","longtemps","lors","lorsque","lui","lui-meme","lui-même","là","lès","m","ma","maint","maintenant","mais","malgre","malgré","maximale","me","meme","memes","merci","mes","mien","mienne","miennes","miens","mille","mince","minimale","moi","moi-meme","moi-même","moindres","moins","mon","moyennant","multiple","multiples","même","mêmes","n","na","naturel","naturelle","naturelles","ne","neanmoins","necessaire","necessairement","neuf","neuvième","ni","nombreuses","nombreux","non","nos","notamment","notre","nous","nous-mêmes","nouveau","nul","néanmoins","nôtre","nôtres","o","oh","ohé","ollé","olé","on","ont","onze","onzième","ore","ou","ouf","ouias","oust","ouste","outre","ouvert","ouverte","ouverts","o|","où","p","paf","pan","par","parce","parfois","parle","parlent","parler","parmi","parseme","partant","particulier","particulière","particulièrement","pas","passé","pendant","pense","permet","personne","peu","peut","peuvent","peux","pff","pfft","pfut","pif","pire","plein","plouf","plus","plusieurs","plutôt","possessif","possessifs","possible","possibles","pouah","pour","pourquoi","pourrais","pourrait","pouvait","prealable","precisement","premier","première","premièrement","pres","probable","probante","procedant","proche","près","psitt","pu","puis","puisque","pur","pure","q","qu","quand","quant","quant-à-soi","quanta","quarante","quatorze","quatre","quatre-vingt","quatrième","quatrièmement","que","quel","quelconque","quelle","quelles","quelqu'un","quelque","quelques","quels","qui","quiconque","quinze","quoi","quoique","r","rare","rarement","rares","relative","relativement","remarquable","rend","rendre","restant","reste","restent","restrictif","retour","revoici","revoilà","rien","s","sa","sacrebleu","sait","sans","sapristi","sauf","se","sein","seize","selon","semblable","semblaient","semble","semblent","sent","sept","septième","sera","seraient","serait","seront","ses","seul","seule","seulement","si","sien","sienne","siennes","siens","sinon","six","sixième","soi","soi-même","soit","soixante","son","sont","sous","souvent","specifique","specifiques","speculatif","stop","strictement","subtiles","suffisant","suffisante","suffit","suis","suit","suivant","suivante","suivantes","suivants","suivre","superpose","sur","surtout","t","ta","tac","tant","tardive","te","tel","telle","tellement","telles","tels","tenant","tend","tenir","tente","tes","tic","tien","tienne","tiennes","tiens","toc","toi","toi-même","ton","touchant","toujours","tous","tout","toute","toutefois","toutes","treize","trente","tres","trois","troisième","troisièmement","trop","très","tsoin","tsouin","tu","té","u","un","une","unes","uniformement","unique","uniques","uns","v","va","vais","vas","vers","via","vif","vifs","vingt","vivat","vive","vives","vlan","voici","voilà","vont","vos","votre","vous","vous-mêmes","vu","vé","vôtre","vôtres","w","x","y","z","zut","à","â","ça","ès","étaient","étais","était","étant","été","être","ô"];

googleMapsKey = "AIzaSyBdRHj_DnOYzEHO5oa0RMIWu0Wp9hrKSnY";

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
    {
        from: "GrandPy",
        kind_of: "Google_Maps_answer",
        content: "Google_Maps"
    },
	{
        from: "GrandPy",
        kind_of: "MediaWiki_answer",
        content: ""
    },

];

// Create and display a DOM elment in the tchat area
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
		case "Google_Maps_answer":
			// Text area
			var googleElt = document.createElement("div");
			googleElt.id = "map";
			googleElt.style.visibility = "hidden";
			contentElt.appendChild(googleElt);
			break;
		case "MediaWiki_answer":
			// Text area
			var mediaWikiElt = document.createElement("div");
			mediaWikiElt.id = "wiki";
			mediaWikiElt.style.visibility = "hidden";
			contentElt.appendChild(mediaWikiElt);
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
	
	// Stop-Word parsing process
	var localisationNameChain  = parserMethod(userRequest.value);
	
	// Gather the User's request
	displayPlaceName(localisationNameChain);
	
	// Display maps as answer
	answerAPI(localisationNameChain);

    // API MediaWiki
});

// Parser method to keep major words
function parserMethod(sentence){
	
	// Major words finder
	var allWordsList = [];
	
	// Split and add in a list
	allWordsList = sentence.split(' ');
	console.log("La liste des mots est de : " + allWordsList.length);
	
	//  Keep major words using  stop-words method
	// Replace parse word by O
	for(var i = 0; i < allWordsList.length; i++){
		for (var j = 0; j < parseFr.length; j++){
			if (allWordsList[i] == parseFr[j]){
				allWordsList.splice(i,1, " ");
				}
			}
		};
	// Remove " " word in order to clean list
	for(var i = 0; i < allWordsList.length; i++){
		if (allWordsList[i] == " "){
			allWordsList.splice(i,1);
			i-=1;
			}
	}
	
	//
		
	// Convert list to string chained
	var allWordsChain = allWordsList.join(' ');
	console.log("La liste des mots importants sont : " + allWordsChain);
	
	return allWordsChain;
};

// Add a Grand Py bubble discussion
function displayPlaceName(place){
	var tchat = {
			from: "GrandPy",
			kind_of: "text",
			content: "Oh... Je connais bien "+ place
		};

	// Display User's request
	var tchatElt = createElementDiscussion(tchat);
	contenuElt.appendChild(tchatElt);
	
	};

// answerAPI
function answerAPI(place){

	// Display map in a bubble
	googleMapsAPI(place);
};

// Google Maps API
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

// Media Wiki API
function mediaWikiAPI(place){

	/* Found on Github
	$.get("https://fr.wikipedia.org/w/api.php?origin=*&action=query&titles=" + place + "&prop=revisions&rvprop=content&format=json", function (responseWiki) {
		if (responseWiki === undefined || responseWiki["query"] === undefined || responseWiki["query"]["pages"]["5653202"] === undefined) {
			displayMessage(noStory);
		} else {
			var anecdote = responseWiki["query"]["pages"]["5653202"]["revisions"][0]["*"];
			
			anecdote = anecdote.split("==")[2].split("File")[0];
			anecdote = anecdote.substring(0, 54) + anecdote.substring(56,83) + "." + anecdote.substring(122,141) + " T" + anecdote.substring(158,277);
			anecdote = anecdote.split("[[").join("").split("]]").join("");
			
			var index = Math.floor(Math.random()*stories.length);
			
			story = stories[index];
			displayMessage(story + anecdote);
		}
	});
	*/
};

// Test

/*

const bubbleDiscussion = {
	// Attributes
	from: null,
	kind_of: null,
	content: null,
	
	// Create a DOM element
	creationOfDOM(){
		// DOM element
		var bubbleElt = document.createElement("div");

		// Display
		switch (this.from) {
			case "GrandPy":
				bubbleElt.setAttribute("class","row bubble bubble_right");
				break;
			case "User":
				bubbleElt.setAttribute("class","row bubble bubble_left");
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
		case "Google_Maps_answer":
		// Text area
		var googleElt = document.createElement("div");
		googleElt.id = "map";
		googleElt.style.visibility = "hidden";
		contentElt.appendChild(googleElt);
		break;
		case "MediaWiki_answer":
		// Text area
		var mediaWikiElt = document.createElement("div");
		mediaWikiElt.id = "wiki";
		mediaWikiElt.style.visibility = "hidden";
		contentElt.appendChild(mediaWikiElt);
		break;
		default:
		console.log("Element built not known - Content");
		}
	};
	
};


// Object Programmation
function character(){
	this.name = null;
	this.className = null;
	
	// Initialisation
	this.init(){
		// Give a DOM class name
		switch (this.name){
			case "GrandPy":
				this.className = "row bubble bubble_right";
				break;
			case "User":
				this.className = "row bubble bubble_left";
				break;
			default:
				this.className = "row";
				console.log("Character defined not known");
		};
	};
	
	// DOM element creation
	this.CreationDOM(){
		
		// Create a bubble form discussion
		var bubbleElt = document.createElement("div");
		bubbleElt.setAttribute("class",this.className);
	};
	
	// Display text on monitor
	this.displayText(textToDisplay){
		// DOM element creation
		this.CreationDOM();
		
		// DOM element content
		var textElt = document.createElement("p");
		textElt.textContent = textToDisplay;
		bubbleElt.appendChild(textElt);
	};
	
	// Display a form on monitor
	this.displayForm(){
		// DOM element creation
		this.CreationDOM();
		
		// Input
		var inputElt = document.createElement("input");
		inputElt.id = "User_destination";
		inputElt.setAttribute("placeholder","Tape ton adresse ici!");
		inputElt.setAttribute("maxlength","45");
		bubbleElt.appendChild(inputElt);

		// Button
		var ButtonElt = document.createElement("button");
		ButtonElt.id = "Destination_btn";
		ButtonElt.setAttribute("class","btn btn-primary");
		ButtonElt.setAttribute("type","button");
		ButtonElt.setAttribute("required", "true");
		ButtonElt.appendChild(document.createTextNode("Envoi"));
		bubbleElt.appendChild(ButtonElt);
		break;
	
	};
	
	// Display Map
	this.displayMap(place){
	};
	
	// Display short story
	this.displayStory(place){
	};
	
	// Parser string
	ParseMethod(stringToParse){
		
		// Split and add in a list
		var wordsList = sentence.split(' ');
		console.log("La liste des mots initials est de : " + wordsList.length);
	
		// Keep major words using stop-words method
		// Replace parsed word by " "
		for(var i = 0; i < wordsList.length; i++){
			for (var j = 0; j < parseFr.length; j++){
				if (wordsList[i] == parseFr[j]){
					wordsList.splice(i,1, " ");
					}
				}
			};

		// Remove " " words in order to clean list
		for(var i = 0; i < wordsList.length; i++){
			if (wordsList[i] == " "){
				wordsList.splice(i,1);
				i-=1;
			}
		}
			
		// Convert list to string chained
		var wordsListChain = wordsList.join(' ');
		console.log("La liste des mots importants sont : " + wordsListChain);
		
		return wordsListChain;
	};
	
};

// Character initialisation
var User = new character();
User.name = "User";

var GrandPy = new character();
GrandPy.name = "GrandPy";

// Introduction
GrandPy.displayText("Ou veux tu aller mon pitchoune?");
User.displayForm();

*/
