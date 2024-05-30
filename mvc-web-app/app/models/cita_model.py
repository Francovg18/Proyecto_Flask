from database import db

class Cita(db.Model):
    __tablename__ = 'citas'

    ID_C = db.Column(db.Integer, primary_key=True)
    ID_P = db.Column(db.Integer, db.ForeignKey('pacientes.ID_P'), nullable=False)
    ID_D = db.Column(db.Integer, db.ForeignKey('doctores.ID_D'), nullable=False)
    FechaHora = db.Column(db.DateTime, nullable=False)
    Estado = db.Column(db.String(50), nullable=False)
    Motivo = db.Column(db.String(255))

    paciente = db.relationship('Paciente', back_populates='citas')
    doctor = db.relationship('Doctor', back_populates='citas')
    recordatorios = db.relationship("Recordatorio", back_populates="cita")  # Definición de la relación

    def __init__(self, ID_P, ID_D, FechaHora, Estado, Motivo):
        self.ID_P = ID_P
        self.ID_D = ID_D
        self.FechaHora = FechaHora
        self.Estado = Estado
        self.Motivo = Motivo

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Cita.query.all()

    @staticmethod
    def get_by_id(ID_C):
        return Cita.query.get(ID_C)

    def update(self, ID_P=None, ID_D=None, FechaHora=None, Estado=None, Motivo=None):
        if ID_P is not None:
            self.ID_P = ID_P
        if ID_D is not None:
            self.ID_D = ID_D
        if FechaHora is not None:
            self.FechaHora = FechaHora
        if Estado is not None:
            self.Estado = Estado
        if Motivo is not None:
            self.Motivo = Motivo
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
