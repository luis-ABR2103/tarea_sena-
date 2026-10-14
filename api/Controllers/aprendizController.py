from flask import jsonify, request
from Services.aprendizService import aprendizService
from Services.PersonaService import PersonaService
import MySQLdb


class aprendizController:

    def show():
        data = aprendizService.show()
        return jsonify(data), 200

    def add():
     data = request.get_json()
     campos_req = ["APR_FECHA_NAC", "APR_PER_ID"]
     faltantes = [w for w in campos_req if w not in data]
     if len(faltantes) > 0:
        return jsonify({"faltan parametros": faltantes}), 400

     try:
         creado = aprendizService.add(data)
     except MySQLdb.IntegrityError:
        return jsonify({"mensaje": "La persona no existe o ya es aprendiz"}), 400
     return jsonify(creado), 201

    def delete(uuid):
        try:
            data = aprendizService.delete(uuid)
        except MySQLdb.IntegrityError:
            return (
                jsonify(
                    {
                        "mensaje": "No se puede eliminar: el aprendiz tiene registros relacionados (matriculas)"
                    }
                ),
                409,
            )
        if data == 200:
            return (
                jsonify(
                    {"mensaje": f"Aprendiz eliminado correctamente con uuid : {uuid}"}
                ),
                200,
            )
        else:
            return (
                jsonify({"mensaje": f"No se encontro aprendiz con uuid : {uuid}"}),
                404,
            )

    def update(uuid):
        data = request.get_json()
        campos_req = ["APR_FECHA_NAC", "APR_PER_ID"]
        faltantes = [x for x in campos_req if x not in data]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
        x = aprendizService.update(uuid, data)
        if x:
            return jsonify({"mensaje": f"se actualizo el aprendiz con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el aprendiz con uuid: {uuid}"}), 404
