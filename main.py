from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('index.html')

@app.route('/objectives')
def objectives():
    return render_template('objectives.html')

@app.route('/search')
def search():
    # UR MOOOOMMMMMMMMMMM
    planet = request.args.get('object')
    
    return render_template('research.html', planet=planet)

app.run(debug=True)