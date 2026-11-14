import requests

def fetch_stars():
    # Retrieves the spacecatalog API
    url = "https://spacecatalog.org/api/v1/objects?category=star&limit=200"
    response = requests.get(url)
    
    response.raise_for_status()

    # Shows us the reponse as a dict
    data = response.json()
    ran_list = []
        
    for star in data["objects"]:
        ran_list.append(star)

    # star_name = star["name"]
    # star_type = star["object_type"]
    # star_dist = star["distance_ly"]
    # star_mag = star["mag"]
    # star_const = star["constellation"]
    return ran_list 
