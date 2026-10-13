from flask import jsonify, request
from Services.ImparteServicie import ImparteService
import MySQLdb

class ImparteController:

 def show():
    data = ImparteService.show()
    return jsonify(data), 200


 def add():
     data = request.get_json()
     campos_req = ["IMP_ROL", "IMP_FECHA_ASIGNACION", "IMP_CUR_ID", "IMP_INS_ID"]
     faltantes = [w for w in campos_req if w not in data]
     if len(faltantes) > 0:
         return jsonify({"faltan parametros": faltantes}), 400
 
     try:
         creado = ImparteService.add(data)
     except MySQLdb.IntegrityError:
         return jsonify({"mensaje": "Ya existe una imparticion con ese codigo"}), 409
     return jsonify(creado), 201

 def delete(uuid):
    data = ImparteService.delete(uuid)
    if data == 200:
        return (
            jsonify({"mensaje": f"Imparte eliminado correctamente con uuid : {uuid}"}),
            200,
        )
    else:
        return jsonify({"mensaje": f"No se encontro imparte con uuid : {uuid}"}), 404
    
 def update(uuid):
        data = request.get_json()
        campos_req = ["IMP_ROL", "IMP_FECHA_ASIGNACION", "IMP_CUR_ID", "IMP_INS_ID"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
        x = ImparteService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo la imparticion con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la imparticion con uuid: {uuid}"}), 404


# cyflz16
