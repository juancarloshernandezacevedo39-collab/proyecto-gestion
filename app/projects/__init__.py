from flask import Blueprint, render_template

bp = Blueprint("projects", __name__, url_prefix="/projects")


@bp.route("/")
def index():
    # Reemplazar por la lógica real en el Hito 2
    return render_template("placeholder.html", titulo="Proyectos y fases", hito="Hito 2")
