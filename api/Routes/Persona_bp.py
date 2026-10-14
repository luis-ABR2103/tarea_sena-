from flask import Blueprint
from Controllers.PersonaController import personaController

per_bp = Blueprint('per_bp', __name__)

@per_bp.route('/', methods=['GET'])
def show():
    return personaController.show()

@per_bp.route('/', methods=['POST'])
def add():
    return personaController.add()

@per_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return personaController.delete(uuid)

@per_bp.route('/<uuid>', methods=['PUT'])
def update(uuid):
    return personaController.update(uuid)