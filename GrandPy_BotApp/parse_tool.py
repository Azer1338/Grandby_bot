import json


def parsing_method(sentence, path="GrandPy_BotApp/static/json/Parse_FR.json"):
    """ Keep major words using stop-words method.
    """

    # Load the stop words JSON file
    with open(path, "r") as read_file:
        parse_fr_list = json.load(read_file)

    # Convert a chain into list - splitting by an " "(space) element
    all_words_chain = sentence
    all_words_list = all_words_chain.split(' ')

    # Replace word by "space" word if it is a stop word
    for i, singleWord in enumerate(all_words_list):
        for stop_word in parse_fr_list:
            if singleWord == stop_word:
                all_words_list[i] = "space"

    # Convert a list into chain - adding a " "(space) element between them
    all_words_chain = " ".join(all_words_list)

    # Replace "space" word by a " " element
    for stop_word in parse_fr_list:
        all_words_chain = all_words_chain.replace("space", '')

    # Return result
    parsing_result = all_words_chain

    return parsing_result
