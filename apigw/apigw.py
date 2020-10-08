from flask import Flask, request
from flask import jsonify
import sys
import json
import os
import requests
import random

#----------------------------------------------------------------
SCHOOL_NODE = "http://schools:5000/"
STUDENT_NODE = "http://students:5000/"
EXTERNAL_NODE = "http://external:5000/"


def call_school_api():
    URI = SCHOOL_NODE + "schools"
    print("calling uri", URI)
    resp = requests.get(URI)
    if resp.status_code != 200:
        print("something wrong in API...exiting")
        return {"result": "error"}
    return resp.json()

def call_student_api():
    URI = STUDENT_NODE + "students"
    print("calling uri", URI)
    resp = requests.get(URI)
    if resp.status_code != 200:
        print("something wrong in API...exiting")
        return {"result": "error"}
    return resp.json()

def call_external_api():
    URI = EXTERNAL_NODE + "external"
    print("calling uri", URI)
    resp = requests.get(URI)
    if resp.status_code != 200:
        print("something wrong in API...exiting")
        return {"result": "error"}
    return resp.json()

#print(call_random_api())

# Rest Server
app = Flask(__name__)

@app.route('/schools', methods=['GET'])
def getschools():
    print("Received external request")
    result = call_school_api()
    return jsonify(result)

@app.route('/students', methods=['GET'])
def getstudents():
    print("Received external request")
    result = call_student_api()
    return jsonify(result)

@app.route('/external', methods=['GET'])
def getexternal():
    print("Received external request")
    result = call_external_api()
    return jsonify(result)

def main():
    app.run(host="0.0.0.0", port=8080, debug=True)


if __name__ == '__main__':
    main()
