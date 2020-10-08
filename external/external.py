from flask import Flask, request
from flask import jsonify
import sys
import json
import os
import requests
import random

#----------------------------------------------------------------
apis = ["https://cat-fact.herokuapp.com/facts",
        "https://api.thecatapi.com/v1/breeds",
        "https://api.thecatapi.com/v1/images/search",
        "https://api.thecatapi.com/v1/categories",
        "https://api.thecatapi.com/v1/votes",
        "https://api.thecatapi.com/v1/images"
        ]

def call_random_api():
    URI = random.choice(apis)
    print("calling uri", URI)
    resp = requests.get(URI)
    if resp.status_code != 200:
        print("something wrong in API...exiting")
        return {"result": "error"}
    return resp.json()

#print(call_random_api())

# Rest Server
app = Flask(__name__)

@app.route('/external', methods=['GET'])
def getschools():
    print("Received external request")
    if request.method == 'GET':
        result = call_random_api()
        return jsonify(result)

def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == '__main__':
    main()
