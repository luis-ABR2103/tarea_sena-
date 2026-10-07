class MatEva:
    def __init__(self, MATE_ID, MATE_UUID, MATE_NOTA, MATE_EVA_ID, MATE_MAT_ID):
        self.MATE_ID = MATE_ID
        self.MATE_UUID = MATE_UUID
        self.MATE_NOTA = MATE_NOTA
        self.MATE_EVA_ID = MATE_EVA_ID
        self.MATE_MAT_ID = MATE_MAT_ID

    def to_dict(self):
        return {
            "MATE_ID": self.MATE_ID,
            "MATE_UUID": self.MATE_UUID,
            "MATE_NOTA": self.MATE_NOTA,
            "MATE_EVA_ID": self.MATE_EVA_ID,
            "MATE_MAT_ID": self.MATE_MAT_ID
        }