from flask import Blueprint, request, jsonify
from models.cita_model import Cita
from views.cita_view import render_cita_detail,render_cita_list

# Crear un blueprint para el controlador de citas
cita_bp = Blueprint("cita", __name__)


# Ruta para obtener la lista de citas
@cita_bp.route("/citas", methods=["GET"])
def get_citas():
    citas = Cita.get_all()
    return jsonify(render_cita_list(citas))


# Ruta para obtener una cita específica por su ID
@cita_bp.route("/citas/<int:ID_C>", methods=["GET"])
def get_cita(ID_C):
    cita = Cita.get_by_id(ID_C)
    if cita:
        return jsonify(render_cita_detail(cita))
    return jsonify({"error": "Cita no encontrada"}), 404


# Ruta para crear una nueva cita
@cita_bp.route("/citas", methods=["POST"])
def create_cita():
    data = request.json
    ID_P = data.get("id_paciente")
    ID_D = data.get("id_doctor")
    FechaHora = data.get("fecha_hora")
    Estado = data.get("estado")
    Motivo = data.get("motivo")

    # Validación simple de datos de entrada
    if ID_P is None or ID_D is None or FechaHora is None or not Estado:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear una nueva cita y guardarla en la base de datos
    cita = Cita(ID_P=ID_P, ID_D=ID_D, FechaHora=FechaHora, Estado=Estado, Motivo=Motivo)
    cita.save()

    return jsonify(cita), 201


# Ruta para actualizar una cita existente
@cita_bp.route("/citas/<int:ID_C>", methods=["PUT"])
def update_cita(ID_C):
    cita = Cita.get_by_id(ID_C)

    if not cita:
        return jsonify({"error": "Cita no encontrada"}), 404

    data = request.json
    ID_P = data.get("id_paciente")
    ID_D = data.get("id_doctor")
    FechaHora = data.get("fecha_hora")
    Estado = data.get("estado")
    Motivo = data.get("motivo")

    # Actualizar los datos de la cita
    cita.update(ID_P=ID_P, ID_D=ID_D, FechaHora=FechaHora, Estado=Estado, Motivo=Motivo)

    return jsonify(render_cita_detail(cita))


# Ruta para eliminar una cita existente
@cita_bp.route("/citas/<int:ID_C>", methods=["DELETE"])
def delete_cita(ID_C):
    cita = Cita.get_by_id(ID_C)

    if not cita:
        return jsonify({"error": "Cita no encontrada"}), 404

    # Eliminar la cita de la base de datos
    cita.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
