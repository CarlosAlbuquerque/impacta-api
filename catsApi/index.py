from flask import Flask, jsonify

app = Flask(__name__)

cats = [
    {'id': 1, 'name': 'Katarina', 'age': 5, 'animalBreed': 'Siamese'},
    {'id': 2, 'name': 'Banguela', 'age': 3, 'animalBreed': 'Black Cat'},
    {'id': 3, 'name': 'Margot', 'age': 3, 'animalBreed': 'SRD'},
]

# Endpoint GET para consulta de um especifico gato
@app.route('/cats/<int:cat_id>', methods=['GET'])
def getCat(cat_id):
    cat = None
    for u in cats:
        if u['id'] == cat_id:
            cat = u
            break

    if cat is not None:
        return jsonify(cat), 200
    else:
        return jsonify({'error': 'Cat not found.'}), 404

# Endpoint GET para consulta de todos os gatos
@app.route('/cats', methods=['GET'])
def getAllCats():
    return jsonify(cats), 200
