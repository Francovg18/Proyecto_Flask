from flask import Blueprint, request, jsonify
from models.recordatorio_model import Recordatorio
from views.recordatorio_view import render_recordatorio_detail,render_recordatorio_list

# Crear un blueprint para el controlador de recordatorios
recordatorio_bp = Blueprint("recordatorio", __name__)


# Ruta para obtener la lista de recordatorios
@recordatorio_bp.route("/recordatorios", methods=["GET"])
def get_recordatorios():
    recordatorios = Recordatorio.get_all()
    return jsonify(render_recordatorio_list(recordatorios))


# Ruta para obtener un recordatorio específico por su ID
@recordatorio_bp.route("/recordatorios/<int:ID_R>", methods=["GET"])
def get_recordatorio(ID_R):
    recordatorio = Recordatorio.get_by_id(ID_R)
    if recordatorio:
        return jsonify(render_recordatorio_detail(recordatorio))
    return jsonify({"error": "Recordatorio no encontrado"}), 404


# Ruta para crear un nuevo recordatorio
@recordatorio_bp.route("/recordatorios", methods=["POST"])
def create_recordatorio():
    data = request.json
    ID_C = data.get("id_cita")
    TipoRecordatorio = data.get("tipo_recordatorio")
    FechaHoraEnvío = data.get("fecha_hora_envio")
    Estado = data.get("estado")

    # Validación simple de datos de entrada
    if ID_C is None or not TipoRecordatorio or FechaHoraEnvío is None or not Estado:
        return jsonify({"error": "Faltan datos requeridos"}), 400

    # Crear un nuevo recordatorio y guardarlo en la base de datos
    recordatorio = Recordatorio(ID_C=ID_C, TipoRecordatorio=TipoRecordatorio, FechaHoraEnvío=FechaHoraEnvío, Estado=Estado)
    recordatorio.save()

    return jsonify(render_recordatorio_detail(recordatorio)), 201


# Ruta para actualizar un recordatorio existente
@recordatorio_bp.route("/recordatorios/<int:ID_R>", methods=["PUT"])
def update_recordatorio(ID_R):
    recordatorio = Recordatorio.get_by_id(ID_R)

    if not recordatorio:
        return jsonify({"error": "Recordatorio no encontrado"}), 404

    data = request.json
    ID_C = data.get("id_cita")
    TipoRecordatorio = data.get("tipo_recordatorio")
    FechaHoraEnvío = data.get("fecha_hora_envio")
    Estado = data.get("estado")

    # Actualizar los datos del recordatorio
    recordatorio.update(ID_C=ID_C, TipoRecordatorio=TipoRecordatorio, FechaHoraEnvío=FechaHoraEnvío, Estado=Estado)

    return jsonify(render_recordatorio_detail(recordatorio))


# Ruta para eliminar un recordatorio existente
@recordatorio_bp.route("/recordatorios/<int:ID_R>", methods=["DELETE"])
def delete_recordatorio(ID_R):
    recordatorio = Recordatorio.get_by_id(ID_R)

    if not recordatorio:
        return jsonify({"error": "Recordatorio no encontrado"}), 404

    # Eliminar el recordatorio de la base de datos
    recordatorio.delete()

    # Respuesta vacía con código de estado 204 (sin contenido)
    return "", 204
