from flask import Flask, request, jsonify, render_template
from utils import MedicalInsurence
import config

app = Flask(__name__)

@app.route('/')
def homepage():
    
    return jsonify({'Result':'Success'})


@app.route('/medical_insurence')
def home1():
    
    return render_template('medical_insurence.html')

@app.route('/test')
def test():
    print("Testing HTML Pages")

    return """<html>
            <body>

            <h1>This is heading 1</h1>
            <h2>This is heading 2</h2>
            <h3>This is heading 3</h3>
            <p>My first paragraph.</p>

            </body>
            </html>"""


@app.route('/home')
def home():
    print("Testing Home Page API")

    return render_template('index.html')

@app.route('/predict_charges', methods = ['GET', 'POST'])
def predict_charges():

    if request.method == 'GET':
        data = request.args.get
        print("Data :",data)
        age = int(data('age'))
        gender = data('gender')
        bmi = int(data('bmi'))
        children = int(data('children'))
        smoker = data('smoker')
        region = data('region')

        Obj = MedicalInsurence(age,gender,bmi,children,smoker,region)
        pred_price = Obj.get_predicted_price()
        
        # return jsonify({"Result":f"Predicted Medical Charges == {pred_price}"})
        return render_template('medical_insurence.html', prediction = pred_price)

    elif request.method == 'POST':
        data = request.form
        print("Data :",data)
        age      = data['age']
        gender   = data['gender']
        bmi      = data['bmi']
        children = data['children']
        smoker   = data['smoker']
        region   = data['region']

        Obj = MedicalInsurence(age,gender,bmi,children,smoker,region)
        pred_price = Obj.get_predicted_price()
        
        # return jsonify({"Result":f"Predicted Medical Charges == {pred_price}"})
        return render_template('medical_insurence.html', prediction = pred_price)

    return jsonify({"Message" : "Unsuccessful"})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=config.PORT_NUMBER)
