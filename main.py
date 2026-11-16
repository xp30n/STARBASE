from flask import Flask, render_template, request, session, redirect, url_for
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
            if any(query.lower() in str(value).lower()
               for value in star.values())
            ]
    return render_template("star_page.html", stars=stars, query=query)

@app.route('/assignments')
def assignments():
    # session.clear()
    # redacted_fields = None

    # If there is a random star in session set the randomstar to that session key
    if 'randomStar' in session:
         randomStarInfo = session['randomStar']
    # If there is no random star generated in the sesssion create a new one
    else:
        stars = fetch_stars()
        # Choose a random star from the filtered star list
        randomStar = random.choice(filtered_stars)
        # Update the random star information 
        randomStarInfo = assignStarInfo(randomStar)
        # Save the info in a session's key
        session['randomStar'] = randomStarInfo

    # The four characteristics that can be redacted
    redactable_fields = ["colour", "distance", "constellation", "brightness"]

    # If the redacted fields key exists in session set that key value to the redacted fields variable
    if 'redacted_fields' in session:
        redacted_fields = session['redacted_fields']
    # If the key doesnt exist set the redacted field to randomly select 2 characteristics
    else:
        redacted_fields = random.sample(redactable_fields, 2)
        session['redacted_fields'] = redacted_fields
    app.logger.info(session['redacted_fields'])
    
    return render_template("assignments.html", randomStar= randomStarInfo, redactedFields=redacted_fields)

@app.route('/submitAssignments', methods = ['POST', 'GET'])
def submit_assignments():
    if 'submittedNames' in session:
        session['submittedNames'] = session['submittedNames']
    else:
         session['submittedNames'] = []

    session['submittedNames'].append(request.form['input_name'])
    app.logger.info(session['submittedNames'])
    return redirect(url_for('assignments'))

app.run(debug=True)