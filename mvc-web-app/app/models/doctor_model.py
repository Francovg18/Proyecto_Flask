from database import db

class Doctor(db.Model):
    
    __tablename__="doctors"
    
    id= db.Column(db.Integer, primary_key=True)
    nombre= db.Column(db.String(50), nullable=False)
    especialidad= db.Column(db.String(50), nullable=False)
    email= db.Column(db.Integer, nullable=False)
    fecha= db.Column(db.Date, nullable=False)
    telefono= db.Column(db.String(50), nullable=False)
    honorarios= db.Column(db.String(50), nullable=False)