from flask import Blueprint, request, jsonify
from models.paciente_model import Paciente
from datetime import datetime
from views.paciente_view import render_paciente_detail,render_paciente_list

# Crear un blueprint para el controlador de pacientes
paciente_bp = Blueprint("paciente", __name__)


# Ruta para obtener la lista de pacientes
@paciente_bp.route("/pacientes", methods=["GET"])
def get_pacientes():
    pacientes = Paciente.get_all()
    return jsonify(render_paciente_list(pacientes))


# Ruta para obtener un paciente específico por su ID
@paciente_bp.route("/pacientes/<int:ID_P>", methods=["GET"])
def get_paciente(ID_P):
    paciente = Paciente.get_by_id(ID_P)
    if paciente:
        return jsonify(render_paciente_detail(paciente))
    return jsonify({"error": "Paciente no encontrado"}), 404


# Ruta para crear un nuevo paciente
@paciente_bp.route("/pacientes", methods=["POST"])
def create_paciente():
    data = request.json
    Nombre = data.get("nombre")
    Email = data.get("email")
    Teléfono = data.get("telefono")
    FechaNacimiento_str = data.get("fecha_nacimiento")
    Género = data.get("genero")
    Dirección = data.get("direccion")

    FechaNacimiento = datetime.strptime(FechaNacimiento_str, "%Y-%m-%d")

    # Validación simple de datos de entrada
    if not Nombre or not Email or Teléfono is None or FechaNacimiento is None or not Género or not Dirección:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo paciente y guardarlo en la base de datos
    paciente = Paciente(Nombre=Nombre, Email=Email, Teléfono=Teléfono, FechaNacimiento=FechaNacimiento, Género=Género, Dirección=Dirección)
    paciente.save()

    return jsonify(render_paciente_detail(paciente)), 201


# Ruta para actualizar un paciente existente
@paciente_bp.route("/pacientes/<int:ID_P>", methods=["PUT"])
def update_paciente(ID_P):
    paciente = Paciente.get_by_id(ID_P)

    if not paciente:
        return jsonify({"error": "Paciente no encontrado"}), 404

    data = request.json
    Nombre = data.get("nombre")
    Email = data.get("email")
    Teléfono = data.get("telefono")
    FechaNacimiento = data.get("fecha_nacimiento")
    Género = data.get("genero")
    Dirección = data.get("direccion")

    # Actualizar los datos del paciente
    paciente.update(Nombre=Nombre, Email=Email, Teléfono=Teléfono, FechaNacimiento=FechaNacimiento, Género=Género, Dirección=Dirección)

    return jsonify(render_paciente_detail(paciente))


# Ruta para eliminar un paciente existente
@paciente_bp.route("/pacientes/<int:ID_P>", methods=["DELETE"])
def delete_paciente(ID_P):
    paciente = Paciente.get_by_id(ID_P)

    if not paciente:
        return jsonify({"error": "Paciente no encontrado"}), 404

    # Eliminar el paciente de la base de datos
    paciente.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
