from flask import Flask, render_template, request, session
import random

from api.starGuess import fetch_stars, assignStarInfo
from api.spacecatalog import filtered_stars

app = Flask(__name__)
app.secret_key = 'Leon_Kennedy_Starbase'

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/stars', methods=["GET"])
def star_page():
    stars = filtered_stars
    query = request.args.get("search", "").strip()
    
    if query:
        stars = [
            star for star in filtered_stars 
            if query.lower() in star["name"].lower()
            ]
    return render_template("star_page.html", stars=stars, query=query)

@app.route('/assignments')
def assignments():
    # session.clear()
    # If there is no random star generated in the sesssion create a new one
    if 'randomStar' not in session:
        stars = fetch_stars()
        # Choose a random star from the filtered star list
        randomStar = random.choice(filtered_stars)
        # Update the random star information 
        randomStarInfo = assignStarInfo(randomStar)
        # Save the info in a session's key
        session['randomStar'] = randomStarInfo
    # If there is a random star in session set the randomstar to that session key
    else:
        randomStarInfo = session['randomStar']

    
    return render_template("assignments.html", randomStar= randomStarInfo)

app.run(debug=True)