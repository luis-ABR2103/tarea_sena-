from flask import jsonify, request
from Services.Mat_EvaServices import MatEvaService
import MySQLdb

class matEvaController:

 def show():
        data = MatEvaService.show()
        return jsonify(data), 200


 def add():
     data = request.get_json(silent=True) or {}
     campos_req = [ "MATE_NOTA", "MATE_EVA_ID", "MATE_MAT_ID"]
     faltantes = [w for w in campos_req if w not in data]
     if len(faltantes) > 0:
         return jsonify({"mensaje": "Faltan parametros: " + ", ".join(faltantes), "faltan parametros": faltantes}), 400
 
     try:
         creado = MatEvaService.add(data)
     except MySQLdb.IntegrityError:
         return jsonify({"mensaje": "La matricula o la evaluacion no existen"}), 409
     return jsonify({"mensaje": "Nota registrada correctamente", "mat_eva": creado}), 201


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
        data = request.get_json(silent=True) or {}
        campos_req = ["MATE_NOTA", "MATE_EVA_ID", "MATE_MAT_ID"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"mensaje": "Faltan parametros: " + ", ".join(faltantes), "faltan parametros": faltantes}), 400
        x = MatEvaService.update(uuid, data)
        if x:
            return jsonify({"mensaje": f"se actualizo la mat_eva con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la mat_eva con uuid: {uuid}"}), 404


# cyflz16
