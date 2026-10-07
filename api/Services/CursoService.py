from flask import current_app
from Models.Curso import Curso
import uuid

class CursoService:
    # operaciones CRUD
    # CREATE, READ, UPDATE, DELETE
    @staticmethod
    def add(data):
            uuid_cur = uuid.uuid4() # genera un uuid
            c  = current_app.mysql.connection.cursor()
            sql = """INSERT INTO T_CURSO (CUR_UUID, CUR_NOMBRE, CUR_CODIGO, CUR_DURACION, CUR_COSTO, CUR_DESCRIPCION) 
            VALUES  (%s, %s, %s, %s, %s, %s)""" #consulta parametrizada
            c.execute(sql, (uuid_cur, data['CUR_NOMBRE'], data['CUR_CODIGO'], data['CUR_DURACION'], data['CUR_COSTO'], data['CUR_DESCRIPCION']))
            c.connection.commit() # guarda los cambios
            id = c.lastrowid # devuelve el id del ultimo registro insertado
            c.close()
            respuesta = {"id":id, "CUR_UUID": uuid_cur, "CUR_NOMBRE" : data["CUR_NOMBRE"], "CUR_CODIGO" : data["CUR_CODIGO"],"CUR_DURACION" : data["CUR_DURACION"], "CUR_COSTO" : data["CUR_COSTO"], "CUR_DESCRIPCION" : data["CUR_DESCRIPCION"] }
            return respuesta

    @staticmethod
    def delete(uuid):
                    c = current_app.mysql.connection.cursor()
                    sql = """ DELETE FROM T_CURSO WHERE CUR_UUID = %s"""
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
                UPDATE T_CURSO 
                SET CUR_NOMBRE = %s, CUR_CODIGO = %s, CUR_DURACION = %s, CUR_COSTO = %s, CUR_DESCRIPCION = %s
                WHERE CUR_UUID = %s
            """
            valores = (data["CUR_NOMBRE"], data["CUR_CODIGO"], data["CUR_DURACION"], data["CUR_COSTO"],
                       data["CUR_DESCRIPCION"], uuid)

            cursor = current_app.mysql.connection.cursor()
            cursor.execute(sql, valores)
            current_app.mysql.connection.commit()
    
            filas_afectadas = cursor.rowcount
            cursor.close()
    
            return filas_afectadas > 0
    

    @staticmethod
    def show():
        sql = "SELECT * FROM T_CURSO"
        c  = current_app.mysql.connection.cursor()
        c.execute(sql)
        data = c.fetchall()
        data = [Curso(x[0], x[1], x[2], x[3], x[4], x[5], x[6]).to_dict() for x in data]
        c.close()
        return data
# relacionado todo lo q esta en la base de datos con la clase curso 