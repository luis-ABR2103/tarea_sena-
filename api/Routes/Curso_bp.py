from flask import Blueprint
from Controllers.CursoController import CursoController

cur_bp = Blueprint("cur_bp", __name__)


@cur_bp.route("/", methods=["GET"])
def show():
    return CursoController.show()


@cur_bp.route("/", methods=["POST"])
def add():
    return CursoController.add()


@cur_bp.route("/<uuid>", methods=["DELETE"])
def delete(uuid):
    return CursoController.delete(uuid)

@cur_bp.route('/<uuid>', methods=['PUT'])
def update(uuid):
    return CursoController.update(uuid)
