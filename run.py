from flask import Flask, jsonify, request, render_template
from diabetes_app.functions import get_predict
import config

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('index.html')

@app.route('/diabetic_prediction', methods = ['GET','POST'])
def predict():
    if request.method == 'POST':
        user_data = request.form
        if not user_data:
            return jsonify({"Message": "Please enter some values in the fields"})
        preg = int(user_data['pregnancies'])
        glucose = int(user_data['glucose'])
        bp = int(user_data['bloodpressure'])
        st = int(user_data['skinthickness'])
        insulin = int(user_data['insulin'])
        bmi = float(user_data['bmi'])
        dpf = float(user_data['dpf'])
        age = int(user_data['age'])

        output = get_predict(preg,glucose,bp,st,insulin,bmi,dpf,age)
        
        return render_template('result.html', prediction=output)
        # return jsonify({"Message":f"{output}"})
    else:
        return jsonify({"Message":"Not successfull"})
if __name__ == "__main__":
    app.run(host='0.0.0.0',port=config.DP_PORT)
