from flask import current_app
from Models.Evaluacion import Evaluacion
import uuid


class EvaluacionService:
    # operaciones CRUD
    # CREATE, READ, UPDATE, DELETE
    @staticmethod
    def add(data):
        uuid_eva = uuid.uuid4()  # genera un uuid
        c = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_EVALAUCION (EVA_UUID, EVA_NOMBRE, EVA_CODIGO, EVA_PORCENTAJE, EVA_FECHA) 
                VALUES  (%s, %s, %s, %s, %s)"""  # consulta parametrizada
        c.execute(
            sql,
            (
                uuid_eva,
                data["EVA_NOMBRE"],
                data["EVA_CODIGO"],
                data["EVA_PORCENTAJE"],
                data["EVA_FECHA"],
            ),
        )
        c.connection.commit()  # guarda los cambios
        id = c.lastrowid  # devuelve el id del ultimo registro insertado
        c.close()
        respuesta = {
            "id": id,
            "EVA_UUID": uuid_eva,
            "EVA_NOMBRE": data["EVA_NOMBRE"],
            "EVA_CODIGO": data["EVA_CODIGO"],
            "EVA_PORCENTAJE": data["EVA_PORCENTAJE"],
            "EVA_FECHA": data["EVA_FECHA"],
        }
        return respuesta

    @staticmethod
    def delete(uuid):
                    c = current_app.mysql.connection.cursor()
                    sql = """ DELETE FROM T_EVALAUCION WHERE EVA_UUID = %s"""
                    c.execute(sql, [uuid])
                    c.connection.commit()
                    if c.rowcount > 0:
                        codigo = 200
                    else:
                        codigo = 404
            
                    c.close()
                    return codigo

    @staticmethod
    def update(uuid, data):
            sql = """
                UPDATE T_EVALAUCION 
                SET EVA_NOMBRE = %s, EVA_CODIGO = %s, EVA_PORCENTAJE = %s, EVA_FECHA = %s
                WHERE EVA_UUID = %s
            """
            valores = (data["EVA_NOMBRE"], data["EVA_CODIGO"], data["EVA_PORCENTAJE"], data["EVA_FECHA"], uuid)

            cursor = current_app.mysql.connection.cursor()
            cursor.execute(sql, valores)
            current_app.mysql.connection.commit()
    
            filas_afectadas = cursor.rowcount
            cursor.close()
    
            return filas_afectadas > 0
    

    @staticmethod
    def show():
            sql = "SELECT * FROM T_EVALAUCION"
            c  = current_app.mysql.connection.cursor()
            c.execute(sql)
            data = c.fetchall()
            data = [Evaluacion(x[0], x[1], x[2], x[3], x[4], x[5]).to_dict() for x in data]
            c.close()
            return data

    # relacionado todo lo q esta en la base de datos con la clase evaluacion
