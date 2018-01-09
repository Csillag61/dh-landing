from flask import Flask, request
from random import randint
from flask_cors import CORS
import requests
import sys


app = Flask(__name__)

def random_with_N_digits(n):
    range_start = 10**(n-1)
    range_end = (10**n)-1
    return randint(range_start, range_end)

CORS(app, resources={r"/*": {"origins": "*"}})
@app.route('/getPIN', methods=['GET', 'POST'])
def generate_PIN():
    print(str(request.get_json()), file=sys.stderr)
    data = request.get_json()
    # look up email
    pin = databaseLookupEmail(data['userData']['email']

    # if exists, return PIN + associated data
    # return pin

    # if not exists, generate new pin
    if(!exists):
        print(random_with_N_digits(5))
    # store pin + associated data
        insertNewUser(data)
        return str(random_with_N_digits(5))

    # return PIN + associated data

