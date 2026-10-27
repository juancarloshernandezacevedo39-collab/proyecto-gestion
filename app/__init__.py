from flask import Flask, render_template

from config import Config
from app.extensions import db, migrate, login_manager, csrf, bcrypt


def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    db.init_app(app)
    migrate.init_app(app, db)
    login_manager.init_app(app)
    csrf.init_app(app)
    bcrypt.init_app(app)

    login_manager.login_view = "auth.login"
    login_manager.login_message = "Inicia sesión para continuar."
    login_manager.login_message_category = "warning"
    @login_manager.user_loader
    def load_user(user_id):
        # Provisional: aún no existe el modelo User (Hito 1, parte 1.1).
        return None
    # Importar modelos para que Flask-Migrate los detecte
    from app import models  # noqa: F401

    # Un Blueprint por módulo / hito
    from app.main import bp as main_bp
    from app.auth import bp as auth_bp
    from app.users import bp as users_bp
    from app.projects import bp as projects_bp
    from app.tasks import bp as tasks_bp
    from app.risks import bp as risks_bp
    from app.dashboard import bp as dashboard_bp

    for blueprint in (main_bp, auth_bp, users_bp, projects_bp,
                      tasks_bp, risks_bp, dashboard_bp):
        app.register_blueprint(blueprint)

    @app.errorhandler(403)
    def forbidden(_e):
        return render_template("errors/403.html"), 403

    @app.errorhandler(404)
    def not_found(_e):
        return render_template("errors/404.html"), 404

    return app
