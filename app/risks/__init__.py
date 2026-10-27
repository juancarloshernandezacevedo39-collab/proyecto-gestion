from flask import Blueprint, render_template

bp = Blueprint("risks", __name__, url_prefix="/risks")


@bp.route("/")
def index():
    # Reemplazar por la lógica real en el Hito 4
    return render_template("placeholder.html", titulo="Riesgos y documentación", hito="Hito 4")
