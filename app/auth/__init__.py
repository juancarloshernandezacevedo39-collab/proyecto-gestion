from flask import Blueprint, render_template

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.route("/")
def index():
    # Reemplazar por la lógica real en el Hito 1
    return render_template("placeholder.html", titulo="Autenticación", hito="Hito 1")
