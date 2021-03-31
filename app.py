from flask import Flask,request, url_for, redirect, render_template, session, redirect
from werkzeug.utils import secure_filename
import pickle
import json
import numpy as np
from flask_mail import Mail
import os

with open('config.json','r') as c:
    params = json.load(c)["params"]

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = params['upload_location']

model=pickle.load(open('model.pkl','rb'))

@app.route('/')
def hello_world():
    return render_template("forest_fire.html")



@app.route('/upload',methods=['POST','GET'])
def uploader():
    if(request.method=='POST'):
        f=request.files['file1']
        f.save(os.path.join(app.config['UPLOAD_FOLDER'] ,secure_filename(f.filename)))
        return "Uploaded Successfully"


# @app.route('/predict',methods=['POST','GET'])
# def predict():
#     int_features=[int(x) for x in request.form.values()]
#     final=[np.array(int_features)]
#     print(int_features)
#     print(final)
#     prediction=model.predict_proba(final)
#     output='{0:.{1}f}'.format(prediction[0][1], 2)

#     if output>str(0.5):
#         return render_template('forest_fire.html',pred='Your Forest is in Danger.\nProbability of fire occuring is {}'.format(output),bhai="kuch karna hain iska ab?")
#     else:
#         return render_template('forest_fire.html',pred='Your Forest is safe.\n Probability of fire occuring is {}'.format(output),bhai="Your Forest is Safe for now")






if __name__ == '__main__':
    app.run(debug=True)
