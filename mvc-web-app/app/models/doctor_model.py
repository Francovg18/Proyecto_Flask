from database import db

class Doctor(db.Model):
    __tablename__ = 'doctores'

    ID_D = db.Column(db.Integer, primary_key=True)
    Nombre = db.Column(db.String(100), nullable=False)
    Especialidad = db.Column(db.String(100), nullable=False)
    Email = db.Column(db.String(100), nullable=False)
    Teléfono = db.Column(db.String(15), nullable=False)
    HorariosConsulta = db.Column(db.String(255), nullable=False)

    citas = db.relationship("Cita", back_populates="doctor")

    def __init__(self, Nombre, Especialidad, Email, Teléfono, HorariosConsulta):
        self.Nombre = Nombre
        self.Especialidad = Especialidad
        self.Email = Email
        self.Teléfono = Teléfono
        self.HorariosConsulta = HorariosConsulta

    def save(self):
        db.session.add(self)
        db.session.commit()

    @staticmethod
    def get_all():
        return Doctor.query.all()

    @staticmethod
    def get_by_id(ID_D):
        return Doctor.query.get(ID_D)

    def update(self, Nombre=None, Especialidad=None, Email=None, Teléfono=None, HorariosConsulta=None):
        if Nombre is not None:
            self.Nombre = Nombre
        if Especialidad is not None:
            self.Especialidad = Especialidad
        if Email is not None:
            self.Email = Email
        if Teléfono is not None:
            self.Teléfono = Teléfono
        if HorariosConsulta is not None:
            self.HorariosConsulta = HorariosConsulta
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
