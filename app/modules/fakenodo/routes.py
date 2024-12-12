from flask import jsonify, make_response
from app.modules.fakenodo import fakenodo_bp
import json
"""
Abre el archivo depositions.json que contiene todas las deposiciones.
Lee el contenido del archivo y lo devuelve en formato JSON.
"""
@fakenodo_bp.route('/fakenodo/deposit/depositions', methods=['GET'])
def get_all():
    with open('app/modules/fakenodo/depositions.json') as f:
        data = json.load(f)
    return jsonify(data)
"""
Simula la creación de un nuevo registro devolviendo una respuesta con un mensaje de confirmación y un ID estático.
Utiliza el código de estado 201 Created para indicar éxito en la creación.
"""
@fakenodo_bp.route('/fakenodo/deposit/depositions', methods=['POST'])
def create():
    response = make_response(jsonify({"message": "Deposition created", "id": 1, "conceptrecid": 1}))
    response.status_code = 201
    return response


@fakenodo_bp.route('/fakenodo/deposit/depositions/<int:id>/files', methods=['POST'])
def upload(id):
    response = make_response(jsonify({"message": f"File uploaded to deposition {id}"}))
    response.status_code = 201
    return response


@fakenodo_bp.route('/fakenodo/deposit/depositions/<int:id>/actions/publish', methods=['POST'])
def publish(id):
    response = make_response(jsonify({"message": f"File uploaded to deposition {id}"}))
    response.status_code = 202
    return response
"""
Simula la eliminación de una deposición específica (identificada por el id).
Devuelve un mensaje confirmando que la deposición ha sido eliminada.
"""

@fakenodo_bp.route('/fakenodo/deposit/depositions/<int:id>', methods=['DELETE'])
def delete(id):
    return jsonify({"message": f"Deposition {id} deleted"})

