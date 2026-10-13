from flask import current_app
from Models.Evaluacion import Evaluacion

class EvaluacionService:
    # operaciones CRUD
    # CREATE, READ, UPDATE, DELETE
    @staticmethod
    def add():
        pass

    @staticmethod
    def delete():
        pass

    @staticmethod
    def update():
        pass

    @staticmethod
    def show():
            sql = "SELECT * FROM T_EVALUACION"
            c  = current_app.mysql.connection.cursor()
            c.execute(sql)
            data = c.fetchall()
            data = [ Evaluacion(x[0], x[1], x[2], x[3], x[4], x[5]) for x in data]
            c.close()
            return data
    # relacionado todo lo q esta en la base de datos con la clase evaluacion