from flask import jsonify, request
from Services.InstructorService import InstructorService
import MySQLdb

class InstructorController:

 def show():
        data = InstructorService.show()
        return jsonify(data), 200


 def add():
      data = request.get_json()
      campos_req = ["INS_ESPECIALIDAD", "INS_PER_ID"]
      faltantes = [w for w in campos_req if w not in data]
      if len(faltantes) > 0:
         return jsonify({"faltan parametros": faltantes}), 400
 
      try:
          creado = InstructorService.add(data)
      except MySQLdb.IntegrityError:
         return jsonify({"mensaje": "La persona no existe o ya es instructor"}), 400
      return jsonify(creado), 201


 def delete(uuid):
    data = InstructorService.delete(uuid)
    if data == 200:
        return (
            jsonify({"mensaje": f"Instructor eliminado correctamente con uuid : {uuid}"}),
            200,
        )
    else:
        return jsonify({"mensaje": f"No se encontro instructor con uuid : {uuid}"}), 404
    
 def update(uuid):
     data = request.get_json()
     campos_req = ["INS_ESPECIALIDAD", "INS_PER_ID"]
     faltantes = [x for x in campos_req if x not in data]
     if len(faltantes) > 0:
         return jsonify({"faltan parametros": faltantes}), 400
     x = InstructorService.update(uuid, data)
     if x:
         return jsonify({"mensaje": f"se actualizo la persona con uuid: {uuid}"}), 200
     else:
         return jsonify({"mensaje": f"no se encontro la persona con uuid: {uuid}"}), 404


# cyflz16
