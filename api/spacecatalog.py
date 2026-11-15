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
    
    # Sets the randomStarInfo name
    randomStarInfo["name"] = randomStar['name']
    
    # Sets the randomStarInfo constellation
    randomStarInfo['constellation'] = randomStar['constellation']
    
    # Sets the randomStarInfo distance value
    if randomStar['distance_ly'] < 50:
        randomStarInfo['distance'] = starDistances[0]
    if 50 <= randomStar['distance_ly'] < 500:
        randomStarInfo['distance'] = starDistances[1]
    if 500 <= randomStar['distance_ly'] < 1000:
        randomStarInfo['distance'] = starDistances[2]
    if randomStar['distance_ly'] >= 1000:
         randomStarInfo['distance'] = starDistances[2]
         
    # Check if the star colour name  in the randomStars' object_type matches the name in the starColours list and set the randomStarInfo['colour'] to that colour
    # Checks all the colours in the star colour list
    for colour in starColours:
        # Checks if that colour exists in the object_type string
        if colour in randomStar["object_type"]:
            # If it exists set that colour match to be the randomstars' colour info
            randomStarInfo["colour"] = colour
            # Break out of the loop once the colour match is found
            break
   
    
    # star_name = star["name"]
    # star_type = star["object_type"]
    # star_dist = star["distance_ly"]
    # star_mag = star["mag"]
    # star_const = star["constellation"]
    return ran_list, randomStarInfo
