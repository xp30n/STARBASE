from flask import Flask, render_template, request, session, redirect, url_for
import random
import os
import json

from api.starGuess import fetch_stars, assignStarInfo, randomStarInfo
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
    if 'starMatch' not in session:
         session['starMatch'] = False
        
    # If there is a random star in session set the randomstar to that session key
    if 'randomStar' in session:
         randomStarInfoCopy = session['randomStar']
    # If there is no random star generated in the sesssion create a new one
    else:
        # Choose a random star from the filtered star list
        randomStar = random.choice(filtered_stars)
        
        assignStarInfo(randomStar)
        # Update the random star information 
        randomStarInfoCopy = randomStarInfo.copy()
        # Save the info in a session's key
        session['randomStar'] = randomStarInfoCopy

    # The four characteristics that can be redacted
    redactable_fields = ["colour", "distance", "constellation", "brightness"]

    # If the redacted fields key exists in session set that key value to the redacted fields variable
    if 'redacted_fields' in session:
        redacted_fields = session['redacted_fields']
    # If the key doesnt exist set the redacted field to randomly select 2 characteristics
    else:
        redacted_fields = random.sample(redactable_fields, 2)
        session['redacted_fields'] = redacted_fields
    app.logger.info(session['starMatch'])
    return render_template("assignments.html", randomStar= randomStarInfoCopy, redactedFields=redacted_fields, starMatch = session['starMatch'])


@app.route('/submitAssignments', methods = ['POST', 'GET'])
def submit_assignments():
    if 'submittedNames' in session:
        session['submittedNames'] = session['submittedNames']
    else:
         session['submittedNames'] = []

    session['submittedNames'].append(request.form['input_name'])
    currentGuess = session['submittedNames'][-1]
    if session['randomStar']['name'].lower() == currentGuess.lower():
        starMatch = True
    else:
        starMatch = False
    app.logger.info(session['submittedNames'], starMatch)
    session['starMatch'] = starMatch
    return redirect(url_for('assignments'))


@app.route('/assignmentsDone', methods = ['POST'])
def did_assignments():
    data = request.get_json()
    filePath="userDatafiles/starInputData.json"
    if os.path.exists(filePath):
        jsonFile = ""
        app.logger.info("file exists")
        jsonFile = open(filePath, "r")
        submittedNamesList = []
        submittedNamesList = json.load(jsonFile)
        submittedNamesList.append(session['submittedNames'])
        jsonFile.close()
        jsonFile_write = open(filePath, "w")
        json.dump(submittedNamesList, jsonFile_write, indent =4)
        jsonFile_write.close()
        
    else:
        app.logger.info("file not exists")
        #open file for writing
        jsonFile = open(filePath, "w")
        inputedNamesList = [session['submittedNames']]
        json.dump(inputedNamesList, jsonFile, indent =4)
        jsonFile.close()

    button_clicked = data.get('buttonClicked')

    if button_clicked and session.get('starMatch'):

        session['starMatch'] = False
        session.pop('randomStar')
        session.pop('redacted_fields')
        session.pop('submittedNames')
        
    return '', 204

app.run(debug=True)