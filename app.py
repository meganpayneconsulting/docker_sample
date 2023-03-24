from joblib import load
import numpy as np
from flask import Flask, request, jsonify
from sklearn.preprocessing import StandardScaler


app = Flask(__name__)

# load the saved model 
filename = 'final_model.sav'
model = load(filename)
scaler = load('scaler_fit.sav')

@app.route('/predict', methods=['GET', 'POST'])
def predict_penguin():
    if request.method == 'GET':
        new_data = request.get_json()
    elif request.method == 'POST':
        new_data = request.get_json()
        print(f"{new_data} NEW DATA")
    X_new = new_data['X_new']
    X_new = np.array(list(map(float, X_new.split(',')))).reshape(1, -1)
    X_new = scaler.fit_transform(X_new)
    pred = model.predict(X_new)
    return jsonify({'predicted class': pred.tolist()})

if __name__ == '__main__':
    app.run(port=5000, host='0.0.0.0', debug=True)