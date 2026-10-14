class Curso:
    def __init__(self, CUR_ID, CUR_UUID, CUR_NOMBRE, CUR_CODIGO, CUR_DURACION, CUR_COSTO, CUR_DESCRIPCION):
        self.CUR_ID = CUR_ID
        self.CUR_UUID = CUR_UUID
        self.CUR_NOMBRE = CUR_NOMBRE
        self.CUR_CODIGO = CUR_CODIGO
        self.CUR_DURACION = CUR_DURACION
        self.CUR_COSTO = CUR_COSTO
        self.CUR_DESCRIPCION = CUR_DESCRIPCION

    def to_dict(self):
        return {
            "CUR_ID": self.CUR_ID,
            "CUR_UUID": self.CUR_UUID,
            "CUR_NOMBRE": self.CUR_NOMBRE,
            "CUR_CODIGO": self.CUR_CODIGO,
            "CUR_DURACION": self.CUR_DURACION,
            "CUR_COSTO": self.CUR_COSTO,
            "CUR_DESCRIPCION": self.CUR_DESCRIPCION
        }