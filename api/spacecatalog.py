import json, random
from api.starGuess import fetch_stars, assignStarInfo

stars = fetch_stars()

# Filter out the stars with special characters
filtered_stars = []

for star in stars:
    # If the name contains any special characters that aren't on a standard keyboard, and if the name only contains letters and numbers
    if star["name"].isascii() and star["name"].replace(" ","").isalnum():
        # If the star passes inpsection, it gets put into the filtered_stars list and gets put onto the webpage
        filtered_stars.append(star)

for star in filtered_stars:
    starInfo = assignStarInfo(star)
    star.update(starInfo)

# randomStar = random.choice(filtered_stars)
# assignStarInfo(randomStar)