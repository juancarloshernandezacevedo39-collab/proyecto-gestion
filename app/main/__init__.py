from flask import Blueprint, render_template, jsonify

bp = Blueprint("main", __name__)

HITOS = [
    ("Usuarios, roles y autenticación", "auth.index"),
    ("Proyectos y fases", "projects.index"),
    ("Tareas y estimación", "tasks.index"),
    ("Riesgos y documentación", "risks.index"),
    ("Dashboard e informe PDF", "dashboard.index"),
]


@bp.route("/")
def index():
    return render_template("index.html", hitos=HITOS)


@bp.route("/salud")
def salud():
    """Ruta de verificación para el despliegue."""
    return jsonify(estado="ok")
