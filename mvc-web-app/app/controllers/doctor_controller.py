from flask import Blueprint, request, jsonify
from models.doctor_model import Doctor
from views.doctor_view import render_doctor_detail,render_doctor_list

# Crear un blueprint para el controlador de doctores
doctor_bp = Blueprint("doctor", __name__)


# Ruta para obtener la lista de doctores
@doctor_bp.route("/doctores", methods=["GET"])
def get_doctores():
    doctores = Doctor.get_all()
    return jsonify(render_doctor_list(doctores))


# Ruta para obtener un doctor específico por su ID
@doctor_bp.route("/doctores/<int:ID_D>", methods=["GET"])
def get_doctor(ID_D):
    doctor = Doctor.get_by_id(ID_D)
    if doctor:
        return jsonify(doctor)
    return jsonify({"error": "Doctor no encontrado"}), 404


# Ruta para crear un nuevo doctor
@doctor_bp.route("/doctores", methods=["POST"])
def create_doctor():
    data = request.json
    Nombre = data.get("nombre")
    Especialidad = data.get("especialidad")
    Email = data.get("email")
    Teléfono = data.get("telefono")
    HorariosConsulta = data.get("horarios_consulta")

    # Validación simple de datos de entrada
    if not Nombre or not Especialidad or not Email or Teléfono is None or not HorariosConsulta:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo doctor y guardarlo en la base de datos
    doctor = Doctor(Nombre=Nombre, Especialidad=Especialidad, Email=Email, Teléfono=Teléfono, HorariosConsulta=HorariosConsulta)
    doctor.save()

    return jsonify(render_doctor_detail(doctor)), 201


# Ruta para actualizar un doctor existente
@doctor_bp.route("/doctores/<int:ID_D>", methods=["PUT"])
def update_doctor(ID_D):
    doctor = Doctor.get_by_id(ID_D)

    if not doctor:
        return jsonify({"error": "Doctor no encontrado"}), 404

    data = request.json
    Nombre = data.get("nombre")
    Especialidad = data.get("especialidad")
    Email = data.get("email")
    Teléfono = data.get("telefono")
    HorariosConsulta = data.get("horarios_consulta")

    # Actualizar los datos del doctor
    doctor.update(Nombre=Nombre, Especialidad=Especialidad, Email=Email, Teléfono=Teléfono, HorariosConsulta=HorariosConsulta)

    return jsonify(render_doctor_detail(doctor))


# Ruta para eliminar un doctor existente
@doctor_bp.route("/doctores/<int:ID_D>", methods=["DELETE"])
def delete_doctor(ID_D):
    doctor = Doctor.get_by_id(ID_D)

    if not doctor:
        return jsonify({"error": "Doctor no encontrado"}), 404

    # Eliminar el doctor de la base de datos
    doctor.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
