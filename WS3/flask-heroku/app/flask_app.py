from flask import Flask, request, jsonify
from app.bmiCalc import calculate_bmi

app = Flask('__name__')

'''
A function to get the request using flask and return 
the calculated bmi.
'''
@app.route('/', methods=['GET', 'POST'])
def get_input():

    packet = request.get_json(force=True)
    weight = packet['weight']
    height = packet['height']
    bmi = calculate_bmi(weight, height)
    return jsonify(packet, bmi) 

