from database import db

class Recordatorio(db.Model):
    __tablename__ = 'recordatorios'

    ID_R = db.Column(db.Integer, primary_key=True)
    ID_C = db.Column(db.Integer, db.ForeignKey('citas.ID_C'), nullable=False)
    TipoRecordatorio = db.Column(db.String(10), nullable=False)
    FechaHoraEnvío = db.Column(db.DateTime, nullable=False)
    Estado = db.Column(db.String(50), nullable=False)
    ID_P = db.Column(db.Integer, db.ForeignKey('pacientes.ID_P'), nullable=False)  # Añade esta línea

    cita = db.relationship('Cita', back_populates='recordatorios')
    paciente = db.relationship('Paciente', back_populates='recordatorios')

    def __init__(self, ID_C, TipoRecordatorio, FechaHoraEnvío, Estado, ID_P):  # Añade ID_P al constructor
        self.ID_C = ID_C
        self.TipoRecordatorio = TipoRecordatorio
        self.FechaHoraEnvío = FechaHoraEnvío
        self.Estado = Estado
        self.ID_P = ID_P  # Añade esta línea

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Recordatorio.query.all()

    @staticmethod
    def get_by_id(ID_R):
        return Recordatorio.query.get(ID_R)

    def update(self, ID_C=None, TipoRecordatorio=None, FechaHoraEnvío=None, Estado=None, ID_P=None):  # Añade ID_P a los parámetros
        if ID_C is not None:
            self.ID_C = ID_C
        if TipoRecordatorio is not None:
            self.TipoRecordatorio = TipoRecordatorio
        if FechaHoraEnvío is not None:
            self.FechaHoraEnvío = FechaHoraEnvío
        if Estado is not None:
            self.Estado = Estado
        if ID_P is not None:  # Añade esta línea
            self.ID_P = ID_P  # Añade esta línea
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
