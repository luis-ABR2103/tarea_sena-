from flask import jsonify, request
from Services.MatriculaServices import MatriculaService
import MySQLdb

class matriculaController:

 def show():
        data = MatriculaService.show()
        return jsonify(data), 200


 def add():
    data = request.get_json()
    campos_req = ["MAT_ESTADO", "MAT_FECHA_INSCRIPCION", "MAT_CUR_ID", "MAT_APR_ID"]
    faltantes = [w for w in campos_req if w not in data]
    if len(faltantes) > 0:
        return jsonify({"faltan parametros": faltantes}), 400

    try:
        creado = MatriculaService.add(data)
    except MySQLdb.IntegrityError:
        return jsonify({"mensaje": "El aprendiz o el curso no existen"}), 400
    return jsonify(creado), 201


 def delete(uuid):
    data = MatriculaService.delete(uuid)
    if data == 200:
        return (
            jsonify({"mensaje": f"Matricula eliminada correctamente con uuid : {uuid}"}),
            200,
        )
    else:
        return jsonify({"mensaje": f"No se encontro matricula con uuid : {uuid}"}), 404
    
 def update(uuid):
        data = request.get_json()
        campos_req = ["MAT_ESTADO", "MAT_FECHA_INCRIPCION", "MAT_CUR_ID", "MAT_APR_ID"]
        faltantes = [ x for x in campos_req if x not in data ]
        if len(faltantes) > 0:
            return jsonify({"faltan parametros": faltantes}), 400
        x = MatriculaService.update(uuid, data)
        if x == 200:
            return jsonify({"mensaje": f"se actualizo la matricula con uuid: {uuid}"}), 200
        else:
            return jsonify({"mensaje": f"no se encontro la matricula con uuid: {uuid}"}), 404


# cyflz16
