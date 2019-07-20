from GrandPy_BotApp.GoogleMapAPI import GoogleMapAPI
	
def test_geocode_lat():
	
	Home = GoogleMapAPI()
	Home.placeName = "6 Avenue du Ponceau, 95000 Cergy"
	Home.geocode()
	
	assert Home.lat == 49.0393601

def test_geocode_lng():
	
	Home = GoogleMapAPI()
	Home.placeName = "6 Avenue du Ponceau, 95000 Cergy"
	Home.geocode()
	
	assert Home.lng == 2.0723879

def test_init():
	
	Home = GoogleMapAPI()
	
	assert Home.placeName == None

def test_init1():
	
	Home = GoogleMapAPI()
	
	assert Home.lat == None
	
def test_init2():
	
	Home = GoogleMapAPI()
	
	assert Home.lng == None
