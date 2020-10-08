from flask import Flask, request
from flask import jsonify
import sys
import uuid
import json

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
{"name": "suresh", "age": 10, "class": "1st", "section": "a"},
{"name": "ammu", "age": 10, "class": "0", "section": "a"},
{"name": "sakthidurga", "age": 13, "class": "8", "section": "a"},
{"name": "siva", "age": 6, "class": "1st", "section": "a"}
]


for i in initdata:
  i["id"] = generate_id()
  create_kv(i["id"], i)

print("db initialized with ",list_kv())


# Rest Server
app = Flask(__name__)


@app.route('/students', methods=['POST'])
def addstudents():
    if request.method == 'POST':
        content = request.get_json()
        #print json.dumps(content)
        content["id"] = generate_id()
        return jsonify(create_kv(content["id"], content))

@app.route('/students', methods=['GET'])
def getstudents():
    if request.method == 'GET':
        return jsonify(list_kv())

@app.route('/students/<int:id>', methods=['GET'])
def getstudent(id):
    if request.method == 'GET':
        return jsonify(get_kv(id))


@app.route('/students/<int:id>', methods=['PUT'])
def putstudent(id):
    if request.method == 'PUT':
        content = request.get_json()
        return jsonify(update_kv(id, content))


def main():
    app.run(host="0.0.0.0", port=5000, debug=True)


if __name__ == '__main__':
    main()
