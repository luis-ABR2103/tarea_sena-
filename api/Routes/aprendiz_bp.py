# blueprint  
from flask import Blueprint, request
from Controllers.aprendizController import aprendizController

apr_bp = Blueprint('apr_bp', __name__)

@apr_bp.route('/', methods=['GET'])
def show():
    return  aprendizController.show()

@apr_bp.route('/', methods=['POST'])
def add():
    return aprendizController.add()

@apr_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return aprendizController.delete(uuid)

@apr_bp.route('/<uuid>', methods=['PUT'])
def update(uuid):
    return aprendizController.update(uuid)
