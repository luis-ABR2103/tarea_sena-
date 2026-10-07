from flask import current_app
from Models.Persona import Persona
import uuid

class PersonaService:
    # operaciones CRUD
    # CREATE, READ, UPDATE, DELETE
    @staticmethod
    def add(data):
        uuid_apr = uuid.uuid4() # genera un uuid
        c  = current_app.mysql.connection.cursor()
        sql = """INSERT INTO T_PERSONA (PER_UUID, PER_PRI_NOMBRE, PER_SEG_NOMBRE, PER_PRI_APELLIDO, PER_SEG_APELLIDO, PER_DOCUMENTO) VALUES  (%s, %s, %s, %s, %s, %s)""" #consulta parametrizada
        c.execute(sql, (uuid_apr, data['PER_PRI_NOMBRE'], data['PER_SEG_NOMBRE'], data['PER_PRI_APELLIDO'], data['PER_SEG_APELLIDO'], data['PER_DOCUMENTO']))
        c.connection.commit() # guarda los cambios
        id = c.lastrowid # devuelve el id del ultimo registro insertado
        c.close()
        respuesta = {"id":id, "PER_UUID": uuid_apr, "PER_PRI_NOMBRE" : data["PER_PRI_NOMBRE"], "PER_SEG_NOMBRE" : data["PER_SEG_NOMBRE"], "PER_PRI_APELLIDO" : data["PER_PRI_APELLIDO"], "PER_SEG_APELLIDO" : data["PER_SEG_APELLIDO"], "PER_DOCUMENTO" : data["PER_DOCUMENTO"]}
        return respuesta

    @staticmethod
    def delete(uuid):
                    c = current_app.mysql.connection.cursor()
                    sql = """ DELETE FROM T_PERSONA WHERE PER_UUID = %s"""
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
        UPDATE T_PERSONA 
        SET PER_PRI_NOMBRE = %s, PER_SEG_NOMBRE = %s, PER_PRI_APELLIDO = %s, PER_SEG_APELLIDO = %s, PER_DOCUMENTO = %s
        WHERE PER_UUID = %s
     """
     valores = (data["PER_PRI_NOMBRE"], data["PER_SEG_NOMBRE"], data["PER_PRI_APELLIDO"], data["PER_SEG_APELLIDO"], data["PER_DOCUMENTO"], uuid)

     cursor = current_app.mysql.connection.cursor()
     cursor.execute(sql, valores)
     current_app.mysql.connection.commit()

     filas_afectadas = cursor.rowcount
     cursor.close()

     return filas_afectadas > 0

    @staticmethod
    def show():
            sql = "SELECT * FROM T_PERSONA"
            c  = current_app.mysql.connection.cursor()
            c.execute(sql)
            data = c.fetchall()
            data = [ Persona(x[0], x[1], x[2], x[3], x[4], x[5], x[6]).to_dict() for x in data]
            c.close()
            return data
    # relacionado todo lo q esta en la base de datos con la clase persona
    @staticmethod
    def get_by_id(id):
            sql = "SELECT PER_ID FROM T_PERSONA WHERE PER_ID = %s"
            c = current_app.mysql.connection.cursor()
            c.execute(sql,[id])
            data = c.fetchone()
            return data
    
