class Evaluacion:
    def __init__(self, EVA_ID, EVA_UUID, EVA_NOMBRE, EVA_CODIGO, EVA_PORCENTAJE, EVA_FECHA):
        self.EVA_ID = EVA_ID
        self.EVA_UUID = EVA_UUID
        self.EVA_NOMBRE = EVA_NOMBRE
        self.EVA_CODIGO = EVA_CODIGO
        self.EVA_PORCENTAJE = EVA_PORCENTAJE
        self.EVA_FECHA = EVA_FECHA

    def to_dict(self):
        return {
            "EVA_ID": self.EVA_ID,
            "EVA_UUID": self.EVA_UUID,
            "EVA_NOMBRE": self.EVA_NOMBRE,
            "EVA_CODIGO": self.EVA_CODIGO,
            "EVA_PORCENTAJE": self.EVA_PORCENTAJE,
            "EVA_FECHA": str(self.EVA_FECHA) if self.EVA_FECHA else self.EVA_FECHA
        }