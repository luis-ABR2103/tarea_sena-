from flask import Blueprint
from Controllers.EvaluacionController import EvaluacionController

eva_bp = Blueprint('eva_bp', __name__)

@eva_bp.route('/', methods=['GET'])
def show():
    return EvaluacionController.show()

@eva_bp.route('/', methods=['POST'])
def add():
    return EvaluacionController.add()

@eva_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return EvaluacionController.delete(uuid)

@eva_bp.route('/<uuid>', methods=['PUT'])
def update(uuid):
    return EvaluacionController.update(uuid)