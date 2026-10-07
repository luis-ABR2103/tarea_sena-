from flask import Blueprint
from Controllers.ImparteController import ImparteController

imp_bp = Blueprint('imp_bp', __name__)

@imp_bp.route('/', methods=['GET'])
def show():
    return ImparteController.show()

@imp_bp.route('/', methods=['POST'])
def add():
    return ImparteController.add()

@imp_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return ImparteController.delete(uuid)

@imp_bp.route('/<uuid>', methods=['PUT'])
def update(uuid):
    return ImparteController.update(uuid)