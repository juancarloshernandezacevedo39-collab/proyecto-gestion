from flask import Blueprint, render_template

bp = Blueprint("dashboard", __name__, url_prefix="/dashboard")


@bp.route("/")
def index():
    # Reemplazar por la lógica real en el Hito 5
    return render_template("placeholder.html", titulo="Dashboard", hito="Hito 5")
