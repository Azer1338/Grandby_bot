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
            console.log(json_data.result);
            
			// Integration of the json_data
			var map = document.getElementById("map");
			map.innerHTML = json_data.result;
			},
			
		// In case of error
        error : function(resultat, statut, erreur){
			// Message
			console.log("AJAX (Get) function turn crazy");
			}
		});
	});
