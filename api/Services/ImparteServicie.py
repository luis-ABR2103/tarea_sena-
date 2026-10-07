from flask import current_app
from Models.Imparte import Imparte
import uuid


class ImparteService:
    # operaciones CRUD
    # CREATE, READ, UPDATE, DELETE
    @staticmethod
    def add(data):
                uuid_apr = uuid.uuid4()  # genera un uuid
                c = current_app.mysql.connection.cursor()
                sql = """INSERT INTO T_IMPARTE (IMP_UUID, IMP_ROL, IMP_FECHA_ASIGNACION, IMP_CUR_ID, IMP_INS_ID) VALUES  (%s, %s, %s, %s, %s)"""  # consulta parametrizada
                c.execute(sql, (uuid_apr, data["IMP_ROL"], data["IMP_FECHA_ASIGNACION"], data["IMP_CUR_ID"], data["IMP_INS_ID"]))
                c.connection.commit()  # guarda los cambios
                id = c.lastrowid  # devuelve el id del ultimo registro insertado
                c.close()
                respuesta = {
                    "id": id,
                    "IMP_UUID": uuid_apr,
                    "IMP_ROL": data["IMP_ROL"],
                    "IMP_FECHA_ASIGNACION": data["IMP_FECHA_ASIGNACION"],
                    "IMP_CUR_ID": data["IMP_CUR_ID"],
                    "IMP_INS_ID": data["IMP_INS_ID"],
                }
                return respuesta

    @staticmethod
    def delete(uuid):
            c = current_app.mysql.connection.cursor()
            sql = """ DELETE FROM T_IMPARTE WHERE IMP_UUID = %s"""
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
                UPDATE T_IMPARTE
                SET IMP_ROL = %s, IMP_FECHA_ASIGNACION = %s 
                WHERE IMP_UUID = %s
            """
            valores = (data["IMP_ROL"], data["IMP_FECHA_ASIGNACION"], uuid)

            cursor = current_app.mysql.connection.cursor()
            cursor.execute(sql, valores)
            current_app.mysql.connection.commit()
    
            filas_afectadas = cursor.rowcount
            cursor.close()
    
            return filas_afectadas > 0
    @staticmethod
    def show():
        sql = "SELECT * FROM T_IMPARTE"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [Imparte(x[0], x[1], x[2], x[3], x[4], x[5]).to_dict() for x in data]
        c.close()
        return data

    # relacionado todo lo q esta en la base de datos con la clase impartir
