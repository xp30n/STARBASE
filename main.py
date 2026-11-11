from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/objectives')
def objectives():
    return render_template('objectives.html')

@app.route('/facts')
def facts():
    return render_template('/facts.html')
app.run(debug=True)