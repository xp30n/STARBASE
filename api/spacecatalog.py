import requests

# Retrieves the space catalog API
url = "https://spacecatalog.org/api/v1/objects?category=star&limit=200"

# Handles the request
response = requests.get(url)

# Shows us the response as json
data = response.json()

print(data)