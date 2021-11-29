
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

jackson_family = FamilyStructure("Jackson")

@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    members = jackson_family.get_all_members()
    response_body={}
    for indice in range(len(members)):
        response_body["member_"+str(indice)]=members[indice]
    return jsonify(response_body), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_one_member(id):
    member = jackson_family.get_member(id)

    if member:
        response_body = {
            "id": member['id'],
            "first_name": member['first_name'],
            "age": member['age'],
            "lucky_numbers": member['lucky_numbers']
        }
        return jsonify(response_body), 200
    if member is None:
        return jsonify(Error="Miembro no encontrado"), 404

@app.route('/member', methods=['POST'])
def add_member():
    if request.json.get('first_name') is None or request.json.get('age') is None or request.json.get('lucky_numbers') is None:
        return jsonify(), 400
    else:
        first_name = request.json.get('first_name')
        age = int(request.json.get('age'))
        lucky_numbers = request.json.get('lucky_numbers')
        id = request.json.get('id', None)

        member = {
            'first_name': first_name,
            'age': age,
            'lucky_numbers': lucky_numbers,
            'id': id
        }

        jackson_family.add_member(member)

        return jsonify(), 200

@app.route('/member/<int:id>', methods=['DELETE'])
def delete_member(id):

    deleted = jackson_family.delete_member(id)
    if deleted == "Removido":
        return jsonify({'done': True}), 200
    else:
        return jsonify(Error='Not founded'), 404

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
