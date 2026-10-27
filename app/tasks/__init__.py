from flask import Blueprint, render_template

bp = Blueprint("tasks", __name__, url_prefix="/tasks")


@bp.route("/")
def index():
    # Reemplazar por la lógica real en el Hito 3
    return render_template("placeholder.html", titulo="Tareas", hito="Hito 3")
