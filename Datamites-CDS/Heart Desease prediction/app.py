
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
def Diesease():
    st = float(request.form['st'])
    thal = float(request.form['thal'])
    chst = float(request.form['chst'])
    max_rate = float(request.form['max_rate'])    
    X = [[st, thal,chst,max_rate]]
    model = joblib.load('model.pkl')
    heartDieseasePred = model.predict(X)[0]
    return render_template('predict.html',predict=heartDieseasePred)


if __name__ == '__main__':
    app.debug = True
    app.run()

app.run()