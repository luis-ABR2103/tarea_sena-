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
            "IMP_FECHA_ASIGNACION": str(self.IMP_FECHA_ASIGNACION) if self.IMP_FECHA_ASIGNACION else None,  # str() deja la fecha como "AAAA-MM-DD" (sin esto Flask la manda en formato HTTP)
            "IMP_CUR_ID": self.IMP_CUR_ID,
            "IMP_INS_ID": self.IMP_INS_ID
        }