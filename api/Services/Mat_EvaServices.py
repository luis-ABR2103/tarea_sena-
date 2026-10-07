from flask import current_app
from Models.Mat_Eva import MatEva
import uuid


class MatEvaService:
    # operaciones CRUD
    # CREATE, READ, UPDATE, DELETE
    @staticmethod
    def add(data):
                uuid_ins = uuid.uuid4()  # genera un uuid
                c = current_app.mysql.connection.cursor()
                sql = """INSERT INTO T_MAT_EVA (MATE_UUID, MATE_NOTA, MATE_EVA_ID, MATE_MAT_ID) VALUES  (%s, %s, %s, %s)"""  # consulta parametrizada
                c.execute(sql, (uuid_ins, data["MATE_NOTA"], data["MATE_EVA_ID"], data["MATE_MAT_ID"]))
                c.connection.commit()  # guarda los cambios
                id = c.lastrowid  # devuelve el id del ultimo registro insertado
                c.close()
                respuesta = {
                    "id": id,
                    "MATE_UUID": uuid_ins,
                    "MATE_NOTA": data["MATE_NOTA"],
                    "MATE_EVA_ID": data["MATE_EVA_ID"],
                    "MATE_MAT_ID": data["MATE_MAT_ID"],
                }
                return respuesta

    @staticmethod
    def delete(uuid):
        c = current_app.mysql.connection.cursor()
        sql = """ DELETE FROM T_MAT_EVA WHERE MATE_UUID = %s"""
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
                UPDATE T_MAT_EVA 
                SET MATE_NOTA = %s, MATE_EVA_ID = %s, MATE_MAT_ID = %s
                WHERE MATE_UUID = %s
            """
            valores = (data["MATE_NOTA"], data["MATE_EVA_ID"], data["MATE_MAT_ID"], uuid)

            cursor = current_app.mysql.connection.cursor()
            cursor.execute(sql, valores)
            current_app.mysql.connection.commit()
    
            filas_afectadas = cursor.rowcount
            cursor.close()
    
            return filas_afectadas > 0

    @staticmethod
    def show():
        sql = "SELECT * FROM T_MAT_EVA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [MatEva(x[0], x[1], x[2], x[3], x[4]).to_dict() for x in data]
        c.close()
        return data

    # relacionado todo lo q esta en la base de datos con la clase mat_eva
