from flask import Blueprint
from Controllers.InstructorController import InstructorController

ins_bp = Blueprint('ins_bp', __name__)

@ins_bp.route('/', methods=['GET'])
def show():
    return InstructorController.show()

@ins_bp.route('/', methods=['POST'])
def add():
    return InstructorController.add()

@ins_bp.route('/<uuid>', methods=['DELETE'])
def delete(uuid):
    return InstructorController.delete(uuid)

@ins_bp.route('/<uuid>', methods=['PUT'])
def update(uuid):
    return InstructorController.update(uuid)