from flask import Flask, render_template, request, session 

from api.starGuess import fetch_stars
from api.spacecatalog import filtered_stars

app = Flask(__name__)
app.secret_key = 'Leon_Kennedy_Starbase'

@app.route('/')
def homepage():
    
    return render_template('index.html')

@app.route('/stars')
def star_page():
    stars, _ = fetch_stars()
    return render_template("star_page.html", stars=filtered_stars)

@app.route('/assignments')
def assignments():
    # If there is no random star generated in the session
    # Create a new one and 
    if 'randomStar' not in session:
        stars, randomStar = fetch_stars()
        session['randomStar'] = randomStar
    else:
        # The underscore doesnt overwrite the info in the current session
        stars, _ = fetch_stars()
    randomStar = session['randomStar']
    return render_template("assignments.html", stars=stars, randomStar= randomStar)

app.run(debug=True)