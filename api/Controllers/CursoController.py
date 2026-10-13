from flask import jsonify, request
from Services.CursoService import CursoService
import MySQLdb



class CursoController:

 def show():
        data = CursoService.show()
        return jsonify(data), 200

 def add():
    data = request.get_json()
    campos_req = ["CUR_NOMBRE", "CUR_CODIGO", "CUR_DURACION", "CUR_COSTO", "CUR_DESCRIPCION"]
    faltantes = [w for w in campos_req if w not in data]
    if len(faltantes) > 0:
        return jsonify({"faltan parametros": faltantes}), 400

    try:
        creado = CursoService.add(data)
    except MySQLdb.IntegrityError:
        return jsonify({"mensaje": "Ya existe un curso con ese codigo"}), 409
    return jsonify(creado), 201
    
 def delete(uuid):
        data = CursoService.delete(uuid)
        if data == 200:
           return jsonify({"mensaje": f"Curso eliminado correctamente con uuid : {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"No se encontro curso con uuid : {uuid}"}), 404

 def update(uuid):
        data = request.get_json()
        campos_req = ["CUR_NOMBRE", "CUR_CODIGO", "CUR_DURACION", "CUR_COSTO", "CUR_DESCRIPCION"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
        x = CursoService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo el curso con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro el curso con uuid: {uuid}"}), 404

# cyflz16