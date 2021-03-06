from flask import Flask, request, redirect, url_for, flash, jsonify
import numpy as np
import pickle as p
import requests
import json

app = Flask(__name__)


@app.route('/api/', methods=['POST'])
def makecalc():
    data = request.get_json()
    prediction = np.array2string(model.predict(data))
    print(prediction)
    return jsonify(prediction)

if __name__ == '__main__':
    modelfile = 'final_model.pickle'
    model = p.load(open(modelfile, 'rb'))
    app.run(debug=True, host='127.0.0.1')



