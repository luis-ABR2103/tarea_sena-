from flask import current_app
from Models.Instructor import Instructor

class InstructorService:
    # opereraciones CRUD
    # CREATE, READ, UPDATE, DELETE
    def add():
        pass

    def delete():
        pass

    def update():
        pass

    def show():
            sql = "SELECT * FROM T_INSTRUCTOR"
            c  = current_app.mysql.connection.cursor()
            c.execute(sql)
            data = c.fetchall()
            data = [ Instructor(x[0], x[1], x[2], x[3], x[4], x[5]) for x in data]
            c.close()
            return data
    # relacionado todo lo q esta en la base de datos con la clase instructor