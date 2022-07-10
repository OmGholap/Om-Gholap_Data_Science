import flask
from flask import render_template
from flask_cors import CORS
import joblib
from flask import request
import sklearn

app = flask.Flask(__name__,static_url_path='')
CORS(app)

@app.route('/',methods=['GET'])
def sendHomePage():
    return render_template('index.html')

@app.route('/predict',methods=['POST'])
def predictHours():
    hr = float(request.form['hr'])
    X = [[hr]]
    model = joblib.load('model.pkl')
    hours_studied = model.predict(X)[0]
    return render_template('predict.html', predict=hours_studied)

if __name__ == '__main__':
    app.debug = True
    app.run()