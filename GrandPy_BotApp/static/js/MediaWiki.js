
// collect json file from MediaWiki website
console.log("Map created");

$.get({
		// Route destination in views.py
        url: "http://en.wikipedia.org/w/api.php?action=query&list=search&srsearch=pokemon&format=jsonfm",
        // Data to communicate
        data: {query : userRequest.value},
        // In case of succes - launch function
        success: function(data) {
            console.log(data);
            
			/*
			var usRequest = document.getElementById("GrandPyAnswer");
			usRequest.innerHTML = data;
			*/
			},
        error : function(resultat, statut, erreur){
			console.log("AJAX (Get) MediaWiki function turn crazy");
			}
        });
