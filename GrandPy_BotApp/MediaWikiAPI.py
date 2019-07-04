// Media Wiki API
function mediaWikiAPI(place){

	//Found on Github
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
	
};
