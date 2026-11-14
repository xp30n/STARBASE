from flask import Flask, render_template, request 

from api.spacecatalog import fetch_stars

app = Flask(__name__)

@app.route('/')
def homepage():
    
    return render_template('index.html')

@app.route('/stars')
def star_page():
    stars = fetch_stars()
    
    return render_template("star_page.html", stars=stars)

app.run(debug=True)