import requests
# IMPORT RANDOM MODULE
import random
from random import choice

randomStarInfo = {
        'name': None,
        'colour': None,
        'distance': None,
        'constellation': None,
        'brightness': None
    }

randomStar = None 
starColours = ['red', 'orange', 'yellow', 'yellow-white', 'blue', 'blue-white', 'white']
starDistances = ['nearby', 'close', 'distant', 'extremely distant']

def fetch_stars():
    # Retrieves the spacecatalog API
    url = "https://spacecatalog.org/api/v1/objects?category=star&limit=200"
    response = requests.get(url)
    
    response.raise_for_status()

    # Shows us the reponse as a dict
    data = response.json()
    
    # Empty list for random star generation
    ran_list = []
   
    for star in data["objects"]:
        ran_list.append(star)
    randomStar = random.choice(ran_list)

    assignStarInfo(randomStar)

   
    
    # star_name = star["name"]
    # star_type = star["object_type"]
    # star_dist = star["distance_ly"]
    # star_mag = star["mag"]
    # star_const = star["constellation"]
    return ran_list, randomStarInfo

def assignStarInfo(randomizedStar):
    # NAME
    # Sets the randomStarInfo name
    randomStarInfo["name"] = randomizedStar['name']

    # CONSTELLATION
    # Sets the randomStarInfo constellation
    randomStarInfo['constellation'] = randomizedStar['constellation']

    # DISTANCE
    # Sets the randomStarInfo distance value
    # NEARBY
    if randomizedStar['distance_ly'] < 30:
        randomStarInfo['distance'] = starDistances[0]
    # CLOSE
    if 30 <= randomizedStar['distance_ly'] < 200:
        randomStarInfo['distance'] = starDistances[1]
    # DISTANT
    if 200 <= randomizedStar['distance_ly'] < 800:
        randomStarInfo['distance'] = starDistances[2]
    # EXTREMELY DISTANT
    if randomizedStar['distance_ly'] >= 800:
         randomStarInfo['distance'] = starDistances[2]
         
    # Check if the star colour name  in the randomStars' object_type matches the name in the starColours list and set the randomStarInfo['colour'] to that colour
    # Checks all the colours in the star colour list
    for colour in starColours:
        # Checks if that colour exists in the object_type string
        if colour in randomizedStar["object_type"]:
            # If it exists set that colour match to be the randomstars' colour info
            randomStarInfo["colour"] = colour
            # Break out of the loop once the colour match is found
            break