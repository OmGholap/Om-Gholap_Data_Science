
import flask
from flask import request, render_template
from flask_cors import CORS
import joblib

app = flask.Flask(__name__, static_url_path='')
CORS(app)

@app.route('/', methods=['GET'])
def sendHomePage():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predictSpecies():
    drat = float(request.form['drat'])
    hp = float(request.form['hp'])
    X = [[drat, hp]]
    model = joblib.load('model.pkl')
    miles_per_gallon = model.predict(X)[0]
    return render_template('predict.html',predict=miles_per_gallon)


app.run()