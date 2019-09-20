import json

def readfile():
    # Load keys needed
    with open(".env", "r") as read_file:
        file = json.load(read_file)

    return file["GOOGLE_KEY"]

# Kick
#API_GOOGLE_KEY = readfile()