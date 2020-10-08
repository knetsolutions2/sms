from flask import Flask, request
from flask import jsonify
import sys
import uuid
import json
import json
import os
import requests

#----------------------------------------------------------------

# Key Value Store / In Memory DB
in_memory_db = {}


def create_kv(key, value):
    global in_memory_db
    in_memory_db[key] = value
    return in_memory_db[key]

def update_kv(key, value):
    global in_memory_db
    if key in in_memory_db:
        in_memory_db[key] = value
        return in_memory_db[key]
    else:
        return {"error": "key not found"}


def get_kv(key):
    global in_memory_db
    if key in in_memory_db:
        return in_memory_db[key]
    else:
        return {"error": "key not found"}


def list_kv():
    return in_memory_db


# UUID Generation
def generate_uuid():
    return uuid.uuid4()

#
stud_id = 0
def generate_id():
    global stud_id
    stud_id += 1
    return stud_id


initdata = [
{"name": "bvss", "city": "chennai", "type": "cbse" },
{"name": "sunrise", "city": "chennai", "type": "metric" },
{"name": "ghss", "city": "chennai", "type": "state" },
{"name": "global", "city": "chennai", "type": "icse" },
]


for i in initdata:
  i["id"] = generate_id()
  create_kv(i["id"], i)

print("db initialized with ",list_kv())

#----------------------------------------------------------------


STUDENTS_NODE = "http://students:5000/"

def get_students():
    URI = STUDENTS_NODE + "students"
    print("calling uri", URI)
    resp = requests.get(URI)
    if resp.status_code != 200:
        print("something wrong in API...exiting")
        return
    return resp.json()

#----------------------------------------------------------------



# Rest Server
app = Flask(__name__)


@app.route('/school', methods=['POST'])
def addschool():
    if request.method == 'POST':
        content = request.get_json()
        #print json.dumps(content)
        content["id"] = generate_id()
        return jsonify(create_kv(content["id"], content))

@app.route('/schools', methods=['GET'])
def getschools():
    print("Received schools get request")
    if request.method == 'GET':
        students = get_students()
        schools = list_kv()
        result = {"schools": schools, "students" : students}
        return jsonify(result)

@app.route('/schools/<int:id>', methods=['GET'])
def getschool(id):
    if request.method == 'GET':
        return jsonify(get_kv(id))


@app.route('/schools/<int:id>', methods=['PUT'])
def putschool(id):
    if request.method == 'PUT':
        content = request.get_json()
        return jsonify(update_kv(id, content))


def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == '__main__':
    main()
