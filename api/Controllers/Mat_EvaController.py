from flask import jsonify, request
from Services.Mat_EvaServices import MatEvaService
import MySQLdb

class matEvaController:

 def show():
        data = MatEvaService.show()
        return jsonify(data), 200


 def add():
     data = request.get_json()
     campos_req = [ "MATE_NOTA", "MATE_EVA_ID", "MATE_MAT_ID"]
     faltantes = [w for w in campos_req if w not in data]
     if len(faltantes) > 0:
         return jsonify({"faltan parametros": faltantes}), 400
 
     try:
         creado = MatEvaService.add(data)
     except MySQLdb.IntegrityError:
         return jsonify({"mensaje": "Ya existe una mat_eva con ese codigo"}), 409
     return jsonify(creado), 201


 def delete(uuid):
    data = MatEvaService.delete(uuid)
    if data == 200:
        return (
            jsonify({"mensaje": f"Mat_Eva eliminado correctamente con uuid : {uuid}"}),
            200,
        )
    else:
        return jsonify({"mensaje": f"No se encontro mat_eva con uuid : {uuid}"}), 404
    
 def update(uuid):
        data = request.get_json()
        campos_req = [ "MATE_MAT_ID", "MATE_EVA_ID"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
        x = MatEvaService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo la mat_eva con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la mat_eva con uuid: {uuid}"}), 404


# cyflz16
