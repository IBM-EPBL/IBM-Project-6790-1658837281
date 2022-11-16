# import flask from flask import request-as we are getting post and pre reuest,as we are using request we should use render template

from flask import render_template, request
import flask
from flask_cors import CORS
import numpy as np
import joblib

# for secure purpose flask_cors used

app = flask.Flask(__name__, static_url_path="")  # initialize flask file
CORS(app)
model = joblib.load(open('liverdiseaseKNN.pkl', 'rb'))


@app.route('/', methods=['GET'])  # sending get request for asking index.html file
def Home():
    return render_template('index.html')


@app.route("/predict", methods=['POST'])  # with post request it will go to predict.html file
def predict():
    if request.method == 'POST':
        Age = int(request.form[
                      'Age'])  # request.form analyze what ever we given in index.html --this is job for request.form
        Gender = int(request.form['Gender'])
        Total_Bilirubin = float(request.form['Total_Bilirubin'])

        Alkaline_Phosphotase = int(request.form['Alkaline_Phosphotase'])
        Alamine_Aminotransferase = int(request.form['Alamine_Aminotransferase'])
        Aspartate_Aminotransferase = int(request.form['Aspartate_Aminotransferase'])
        Total_Protiens = float(request.form['Total_Protiens'])
        Albumin = float(request.form['Albumin'])
        Albumin_and_Globulin_Ratio = float(request.form['Albumin_and_Globulin_Ratio'])

        # after reading value through request.forms it will store the value in "values"
        # in form of array
        values = np.array([[Age, Gender, Total_Bilirubin, Alkaline_Phosphotase, Alamine_Aminotransferase,
                            Aspartate_Aminotransferase, Total_Protiens, Albumin, Albumin_and_Globulin_Ratio]])
        prediction = model.predict(values)
        # then after storing values this pkl file analyze value inside"values" and we are asking for prediction and we are storing this prediction values inside this prediction
        return render_template('predict.html', prediction=prediction)
        # this prediction shown in predict.html and output will be seen


if __name__ == "__main__":
    app.run(debug=True)