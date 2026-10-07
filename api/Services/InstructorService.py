from flask import current_app
from Models.Instructor import Instructor
import uuid
from Models.Persona import Persona


class InstructorService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add(data):
            uuid_ins = uuid.uuid4()  # genera un uuid
            c = current_app.mysql.connection.cursor()
            sql = """INSERT INTO T_INSTRUCTOR (INS_UUID, INS_ESPECIALIDAD, INS_PER_ID) VALUES  (%s, %s, %s)"""  # consulta parametrizada
            c.execute(sql, (uuid_ins, data["INS_ESPECIALIDAD"], data["INS_PER_ID"]))
            c.connection.commit()  # guarda los cambios
            id = c.lastrowid  # devuelve el id del ultimo registro insertado
            c.close()
            respuesta = {
                "id": id,
                "INS_UUID": uuid_ins,
                "INS_ESPECIALIDAD": data["INS_ESPECIALIDAD"],
                "INS_PER_ID": data["INS_PER_ID"],
            }
            return respuesta

    def delete(uuid):
                c = current_app.mysql.connection.cursor()
                sql = """ DELETE FROM T_INSTRUCTOR WHERE INS_UUID = %s"""
                c.execute(sql, [uuid])
                c.connection.commit()
                if c.rowcount > 0:
                    codigo = 200
                else:
                    codigo = 404
        
                c.close()
                return codigo

    def update(uuid, data):
         sql = """
            UPDATE T_INSTRUCTOR 
            SET INS_ESPECIALIDAD = %s , INS_PER_ID = %s
            WHERE INS_UUID = %s
         """
         valores = (data["INS_ESPECIALIDAD"], data["INS_PER_ID"], uuid)

         cursor = current_app.mysql.connection.cursor()
         cursor.execute(sql, valores)
         current_app.mysql.connection.commit()
    
         filas_afectadas = cursor.rowcount
         cursor.close()
    
         return filas_afectadas > 0
    

    def show():
            sql = """SELECT * FROM T_INSTRUCTOR
                INNER JOIN T_PERSONA ON INS_PER_ID = PER_ID"""
            c = current_app.mysql.connection.cursor()
            c.execute(sql)
            data = c.fetchall()
            print(data)
            data = [Instructor(x[0], x[1], x[2],
                             {"nombres": x[6]+" "+x[7], "apellidos": x[8]+" "+x[9], "cedula": x[10]}
                             ).to_dict() for x in data]
            c.close()
            return data

    # relacionado todo lo q esta en la base de datos con la clase instructor
