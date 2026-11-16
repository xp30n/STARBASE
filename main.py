from flask import Flask, render_template, request, session 

from api.starGuess import fetch_stars

app = Flask(__name__)
app.secret_key = 'Leon_Kennedy_Starbase'

@app.route('/')
def homepage():
    
    return render_template('index.html')

@app.route('/stars')
def star_page():

    
    return render_template("star_page.html")

@app.route('/assignments')
def assignments():
    # session.pop('randomStar')
    # session.pop('stars')
    # session.clear()
    if 'randomStar' not in session:
        stars, randomStar = fetch_stars()
        session['randomStar'] = randomStar
        session['stars'] = stars
    else:
        # The underscore doesnt overwrite the info in the current session
        stars, _ = fetch_stars()

    
    # app.logger.info(stars)
    randomStar = session['randomStar']
    # stars = session['stars']
    
    return render_template("assignments.html", stars=stars, randomStar= randomStar)

app.run(debug=True)