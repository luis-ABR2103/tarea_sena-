class Imparte:
    def __init__(self, IMP_ID, IMP_UUID, IMP_ROL, IMP_FECHA_ASIGNACION, IMP_CUR_ID, IMP_INS_ID):
        self.IMP_ID = IMP_ID
        self.IMP_UUID = IMP_UUID
        self.IMP_ROL = IMP_ROL
        self.IMP_FECHA_ASIGNACION = IMP_FECHA_ASIGNACION
        self.IMP_CUR_ID = IMP_CUR_ID
        self.IMP_INS_ID = IMP_INS_ID

    def to_dict(self):
        return {
            "IMP_ID": self.IMP_ID,
            "IMP_UUID": self.IMP_UUID,
            "IMP_ROL": self.IMP_ROL,
            "IMP_FECHA_ASIGNACION": self.IMP_FECHA_ASIGNACION, #lo q hace es q el JSON no lee los campos DATE Y DATE TIME, Lo q hace el str es convertir la fecha en cadena para q sea compatible con el JSON
            "IMP_CUR_ID": self.IMP_CUR_ID,
            "IMP_INS_ID": self.IMP_INS_ID
        }