from flask import Flask, json, request

fields = [{"id": 1, "name": "Computer Science"}, {"id": 2, "name": "Economics"}]
students = [{"id": 1, "name": "Jan Kowalski"}, {"id": 2, "name": "Karolina Przypadkowa"}]


api = Flask(__name__)

@api.route('/fields', methods=['GET'])
def get_companies():
  return json.dumps(fields)

@api.route('/fields')
def refuse_to_edit():
    return json.dumps({"error": "no access to edit fields resources"}), 403

@api.route("/fields/<id>", methods=['GET'])
def get_fields_by_id(id):
    return get_from_table_by_id(fields, id)

@api.route('/students/<id>', methods=["GET"])
def get_student_by_id(id):
    return get_from_table_by_id(students, id)

def get_from_table_by_id(table, idx):
    for element in table:
        print(element)
        if element["id"] == int(idx):
            return json.dumps(element), 200
    return json.dumps({"error":"id: "+idx+" not found"}), 403


if __name__ == '__main__':
    api.run() 
