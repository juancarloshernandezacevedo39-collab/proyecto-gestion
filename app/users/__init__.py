from flask import Blueprint, render_template

bp = Blueprint("users", __name__, url_prefix="/users")


@bp.route("/")
def index():
    # Reemplazar por la lógica real en el Hito 1
    return render_template("placeholder.html", titulo="Usuarios", hito="Hito 1")
