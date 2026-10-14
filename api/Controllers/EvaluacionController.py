from flask import jsonify, request
from Services.EvaluacionServices import EvaluacionService
import MySQLdb



class EvaluacionController:

 def show():
        data = EvaluacionService.show()
        return jsonify(data), 200

 def add():
    data = request.get_json()
    campos_req = ["EVA_NOMBRE", "EVA_CODIGO", "EVA_PORCENTAJE", "EVA_FECHA"]
    faltantes = [w for w in campos_req if w not in data]
    if len(faltantes) > 0:
        return jsonify({"faltan parametros": faltantes}), 400

    try:
        creado = EvaluacionService.add(data)
    except MySQLdb.IntegrityError:
        return jsonify({"mensaje": "Ya existe una evaluacion con ese codigo"}), 409
    return jsonify(creado), 201
    
 def delete(uuid):
        data = EvaluacionService.delete(uuid)
        if data == 200:
           return jsonify({"mensaje": f"Evaluacion eliminada correctamente con uuid : {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"No se encontro evaluacion con uuid : {uuid}"}), 404
        

 def update(uuid):
        data = request.get_json()
        campos_req = ["EVA_NOMBRE", "EVA_CODIGO", "EVA_PORCENTAJE", "EVA_FECHA"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
        x = EvaluacionService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo la evaluacion con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la evaluacion con uuid: {uuid}"}), 404

# cyflz16