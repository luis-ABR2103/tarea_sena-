from flask import current_app
from Models.Matricula import Matricula
import uuid


class MatriculaService:
    # operaciones CRUD
    # CREATE, READ, UPDATE, DELETE
    @staticmethod
    @staticmethod
    def add(data):
     uuid_mat = str(uuid.uuid4())
     c = current_app.mysql.connection.cursor()
     sql = """INSERT INTO T_MATRICULA (MAT_UUID, MAT_ESTADO, MAT_FECHA_INSCRIPCION, MAT_APR_ID, MAT_CUR_ID) VALUES (%s, %s, %s, %s, %s)"""
     c.execute(sql, (uuid_mat, data["MAT_ESTADO"], data["MAT_FECHA_INSCRIPCION"], data["MAT_APR_ID"], data["MAT_CUR_ID"]))
     c.connection.commit()
     id_nuevo = c.lastrowid
     c.close()
     return Matricula(id_nuevo, uuid_mat, data["MAT_ESTADO"], data["MAT_FECHA_INSCRIPCION"], data["MAT_APR_ID"], data["MAT_CUR_ID"]).to_dict()

    @staticmethod
    def delete(uuid):
                c = current_app.mysql.connection.cursor()
                sql = """ DELETE FROM T_MATRICULA WHERE MAT_UUID = %s"""
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
                UPDATE T_MATRICULA 
                SET MAT_ESTADO = %s, MAT_FECHA_INSCRIPCION = %s, MAT_APR_ID = %s, MAT_CUR_ID = %s
                WHERE MAT_UUID = %s
            """
        valores = (
            data["MAT_ESTADO"],
            data["MAT_FECHA_INSCRIPCION"],
            data["MAT_APR_ID"],
            data["MAT_CUR_ID"],
            uuid,
        )

        cursor = current_app.mysql.connection.cursor()
        cursor.execute(sql, valores)
        current_app.mysql.connection.commit()

        filas_afectadas = cursor.rowcount
        cursor.close()

        return filas_afectadas > 0

    @staticmethod
    def show():
        sql = "SELECT * FROM T_MATRICULA"
        c = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [Matricula(x[0], x[1], x[2], x[3], x[4], x[5]).to_dict() for x in data]
        c.close()
        return data

    # relacionado todo lo q esta en la base de datos con la clase matricula
