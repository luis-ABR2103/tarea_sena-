from flask import current_app
from Models.Mat_Eva    import MatEva

class MatEvaService:
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
            sql = "SELECT * FROM T_MAT_EVA"
            c  = current_app.mysql.connection.cursor()
            c.execute(sql)
            data = c.fetchall()
            data = [ MatEva(x[0], x[1], x[2], x[3], x[4]) for x in data]
            c.close()
            return data
    # relacionado todo lo q esta en la base de datos con la clase mat_eva