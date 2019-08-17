import json


def parsing_method(sentence):
    """ Keep major words using stop-words method.
    """

    # Load the stop words JSON file
    with open("GrandPy_BotApp/static/json/Parse_FR.json", "r") as read_file:
        parse_FR_list = json.load(read_file)

    # Convert a chain into list - splitting by an " "(space) element
    allWordsChain = sentence
    allWordsList = allWordsChain.split(' ')

    # Replace word by "space" word if it is a stop word
    for i, singleWord in enumerate(allWordsList):
        for stop_word in parse_FR_list:
            if singleWord == stop_word:
                allWordsList[i] = "space"

    # Convert a list into chain - adding a " "(space) element between them
    allWordsChain = " ".join(allWordsList)

    # Replace "space" word by a " " element
    for stopword in parse_FR_list:
        allWordsChain = allWordsChain.replace("space", '')

    # Return result
    parsing_result = allWordsChain
    
    return parsing_result
