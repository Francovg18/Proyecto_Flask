from flask import Flask
from controllers.paciente_controller import paciente_bp
from controllers.doctor_controller import doctor_bp
from controllers.cita_controller import cita_bp
from controllers.recordatorio_controller import recordatorio_bp
from flask_swagger_ui import get_swaggerui_blueprint
from database import db

app = Flask(__name__)

# Configura la URL de la documentación OpenAPI
SWAGGER_URL = "/api/docs"  # Ruta para servir Swagger UI
API_URL = "/static/swagger.json"  # Ruta de tu archivo OpenAPI/Swagger
# Inicializa el Blueprint de Swagger UI
swagger_ui_blueprint = get_swaggerui_blueprint(
    SWAGGER_URL, API_URL, config={"app_name": "Sistema de Gestión Médica API"}
)
app.register_blueprint(swagger_ui_blueprint, url_prefix=SWAGGER_URL)

# Configuración de la base de datos
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///medical_system.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# Inicializa la base de datos
db.init_app(app)

# Registra los blueprints de las entidades en la aplicación
app.register_blueprint(paciente_bp, url_prefix="/api")
app.register_blueprint(doctor_bp, url_prefix="/api")
app.register_blueprint(cita_bp, url_prefix="/api")
app.register_blueprint(recordatorio_bp, url_prefix="/api")

# Crea las tablas si no existen
with app.app_context():
    db.create_all()

# Ejecuta la aplicación
if __name__ == "__main__":
    app.run(debug=True)
