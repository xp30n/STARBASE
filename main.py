from flask import Flask, render_template, request 

from api.starGuess import fetch_stars

app = Flask(__name__)

@app.route('/')
def homepage():
    
    return render_template('index.html')

@app.route('/stars')
def star_page():

    
    return render_template("star_page.html")

@app.route('/assignments')
def assignments():
    stars, randomStar = fetch_stars()
    return render_template("assignments.html", stars=stars, randomStar= randomStar)

app.run(debug=True)