import json

def readfile():
    # Load the stop words JSON file
    with open(".env", "r") as read_file:
        file = json.load(read_file)

    #API_GOOGLE_KEY = file["GOOGLE_KEY"]

    return file["GOOGLE_KEY"]

# Kick
API_GOOGLE_KEY = readfile()