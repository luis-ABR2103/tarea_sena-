from flask import jsonify, request
from Services.PersonaService import PersonaService
import MySQLdb


class personaController:

 def show():
        data = PersonaService.show()
        return jsonify(data), 200


 def add():
    data = request.get_json(silent=True)
    if not isinstance(data, dict):
        return jsonify({"mensaje": "El cuerpo debe ser un JSON valido"}), 400

    campos_req = ["PER_PRI_NOMBRE", "PER_PRI_APELLIDO", "PER_DOCUMENTO"]
    faltantes = [w for w in campos_req if not data.get(w)]
    if len(faltantes) > 0:
        return jsonify({"faltan parametros": faltantes}), 400

    try:
        creada = PersonaService.add(data)
    except MySQLdb.IntegrityError:
        return jsonify({"mensaje": "Ya existe una persona con ese documento"}), 409
    return jsonify({"mensaje": "Persona creada correctamente", "persona": creada}), 201
    


 def delete(uuid):
    data = PersonaService.delete(uuid)
    if data == 200:
        return (
            jsonify({"mensaje": f"Persona eliminada correctamente con uuid : {uuid}"}),
            200,
        )
    else:
        return jsonify({"mensaje": f"No se encontro persona con uuid : {uuid}"}), 404
    
 def update(uuid):
    data = request.get_json()
    campos_req = ["PER_PRI_NOMBRE", "PER_SEG_NOMBRE", "PER_PRI_APELLIDO", "PER_SEG_APELLIDO", "PER_DOCUMENTO"]
    faltantes = [x for x in campos_req if x not in data]
    if len(faltantes) > 0:
        return jsonify({"faltan parametros": faltantes}), 400
    x = PersonaService.update(uuid, data)
    if x:
        return jsonify({"mensaje": f"se actualizo la persona con uuid: {uuid}"}), 200
    else:
        return jsonify({"mensaje": f"no se encontro la persona con uuid: {uuid}"}), 404


# cyflz16
