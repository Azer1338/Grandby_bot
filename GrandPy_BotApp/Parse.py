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
