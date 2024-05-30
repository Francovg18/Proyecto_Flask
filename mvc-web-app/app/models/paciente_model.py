from database import db

class Paciente(db.Model):
    __tablename__ = 'pacientes'

    ID_P = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Teléfono = db.Column(db.String(15), nullable=False)
    FechaNacimiento = db.Column(db.Date, nullable=False)
    Género = db.Column(db.String(10), nullable=False)
    Dirección = db.Column(db.String(255), nullable=False)

    citas = db.relationship("Cita", back_populates="paciente")
    recordatorios = db.relationship("Recordatorio", back_populates="paciente")

    def __init__(self, Nombre, Email, Teléfono, FechaNacimiento, Género, Dirección):
        self.Nombre = Nombre
        self.Email = Email
        self.Teléfono = Teléfono
        self.FechaNacimiento = FechaNacimiento
        self.Género = Género
        self.Dirección = Dirección

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Paciente.query.all()

    @staticmethod
    def get_by_id(ID_P):
        return Paciente.query.get(ID_P)

    def update(self, Nombre=None, Email=None, Teléfono=None, FechaNacimiento=None, Género=None, Dirección=None):
        if Nombre is not None:
            self.Nombre = Nombre
        if Email is not None:
            self.Email = Email
        if Teléfono is not None:
            self.Teléfono = Teléfono
        if FechaNacimiento is not None:
            self.FechaNacimiento = FechaNacimiento
        if Género is not None:
            self.Género = Género
        if Dirección is not None:
            self.Dirección = Dirección
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
