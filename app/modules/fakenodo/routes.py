import os
import uuid
import json
from flask import jsonify, make_response, request
from app.modules.fakenodo import fakenodo_bp

DATA_FOLDER = 'app/modules/fakenodo'


# Función auxiliar para cargar archivos JSON
def load_json_file(filename):
    try:
        with open(os.path.join(DATA_FOLDER, filename)) as f:
            return json.load(f)
    except FileNotFoundError:
        return {"error": f"Archivo {filename} no encontrado"}
    except json.JSONDecodeError:
        return {"error": "Error al decodificar el archivo JSON"}


# Función auxiliar para estandarizar respuestas
def create_response(message, status_code=200, **kwargs):
    response = {"message": message}
    response.update(kwargs)
    return make_response(jsonify(response), status_code)


@fakenodo_bp.route('/fakenodo/deposit/depositions', methods=['GET'])
def get_all():
    """
    Recupera todos los depositions del archivo JSON.
    """
    data = load_json_file('depositions.json')
    if "error" in data:
        return create_response(data["error"], 500)
    return jsonify(data)


@fakenodo_bp.route('/fakenodo/deposit/depositions', methods=['POST'])
def create():
    """
    Crea un nuevo deposition con ID dinámico.
    """
    deposition_id = uuid.uuid4().int & (1 << 32) - 1  # Genera un ID aleatorio entero
    conceptrecid = deposition_id

    return create_response(
        "Deposition creado exitosamente",
        201,
        id=deposition_id,
        conceptrecid=conceptrecid
    )


@fakenodo_bp.route('/fakenodo/deposit/depositions/<int:id>/files', methods=['POST'])
def upload(id):
    """
    Simula la subida de un archivo a un deposition.
    """
    return create_response(f"Archivo subido correctamente al deposition {id}", 201)


@fakenodo_bp.route('/fakenodo/deposit/depositions/<int:id>/actions/publish', methods=['POST'])
def publish(id):
    """
    Publica un deposition específico.
    """
    return create_response(f"Deposition {id} publicado exitosamente", 202)


@fakenodo_bp.route('/fakenodo/deposit/depositions/<int:id>', methods=['DELETE'])
def delete(id):
    """
    Elimina un deposition específico.
    """
    return create_response(f"Deposition {id} eliminado exitosamente", 200)


@fakenodo_bp.route('/fakenodo/deposit/depositions/<int:id>', methods=['GET'])
def get_deposition(id):
    """
    Recupera un deposition específico y genera un DOI dinámico.
    """
    data = load_json_file('deposition.json')
    if "error" in data:
        return create_response(data["error"], 500)

    data['id'] = id
    data['doi'] = str(uuid.uuid4())  # Genera un DOI aleatorio
    return jsonify(data)
