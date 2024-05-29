from database import db

class Paciente(db.Model):

    __tablename__="patients"
    
    id= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(50), nullable=False)
    email= db.Column(db.String(50), nullable=False)
    telefono= db.Column(db.Integer, nullable=False)
    fecha= db.Column(db.Date, nullable=False)
    genero= db.Column(db.String(50), nullable=False)
    direccion= db.Column(db.String(50), nullable=False)
    
    citas = db.relationship("Cita", back_populates="paciente")
    # Relación uno a muchos con Recordatorio
    recordatorios = db.relationship("Recordatorio", back_populates="paciente")