import requests, random

# =================================
# STAR CATEGORIES
# =================================
randomStarInfo = {
        'name': None,
        'colour': None,
        'distance': None,
        'constellation': None,
        'brightness': None
    }
    
randomStar = None 
starColours = ['red', 'orange', 'yellow-white', 'yellow', 'blue-white', 'blue', 'white']
starDistances = ['Nearby', 'Close', 'Distant', 'Extremely Distant']
starMag = ['Dim', 'Moderately Bright', 'Bright', 'Very Bright']

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
    
    return ran_list, randomStarInfo


def assignStarInfo(randomizedStar):
    # NAME
    randomStarInfo["name"] = randomizedStar['name']

    # CONSTELLATION 
    randomStarInfo['constellation'] = randomizedStar['constellation']
    
    # MAGNITUDE / BRIGHTNESS
    # DIM
    # =================================
    if randomizedStar['mag'] >= 5:
        randomStarInfo['brightness'] = starMag[0]
    # MODERATELY BRIGHT
    elif 2 <= randomizedStar['mag'] < 5:
        randomStarInfo['brightness'] = starMag[1]
    # BRIGHT
    elif 0 <= randomizedStar['mag'] < 2:
        randomStarInfo['brightness'] = starMag[2]
    # VERY BRIGHT
    else:
        randomStarInfo['brightness'] = starMag[3]
    
        
    # DISTANCE
    # NEARBY
    # =================================
    if randomizedStar['distance_ly'] is not None:
        if randomizedStar['distance_ly'] < 30:
            randomStarInfo['distance'] = starDistances[0]
        # CLOSE
        elif 30 <= randomizedStar['distance_ly'] < 200:
            randomStarInfo['distance'] = starDistances[1]
        # DISTANT
        elif 200 <= randomizedStar['distance_ly'] < 1000:
            randomStarInfo['distance'] = starDistances[2]
        # EXTREMELY DISTANT
        else:
            randomStarInfo['distance'] = starDistances[3]
        
         
    # Check if the star colour name  in the randomStars' object_type matches the name in the 
    # starColours list and set the randomStarInfo['colour'] to that colour
    # Checks all the colours in the star colour list
    for colour in starColours:
        # Checks if that colour exists in the object_type string
        if colour in randomizedStar["object_type"]:
            # If it exists set that colour match to be the randomstars' colour info
            randomStarInfo["colour"] = colour.capitalize()
            # Break out of the loop once the colour match is found
            break
    return randomStarInfo