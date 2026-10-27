"""Modelos de la aplicación.

Cada hito agrega sus modelos aquí (un archivo por entidad) y los importa abajo
para que Flask-Migrate los detecte:

    Hito 1: user.py      -> User, Role
    Hito 2: project.py   -> Project, ProjectMember, Phase
    Hito 3: task.py      -> Task
    Hito 4: risk.py      -> Risk, Document

Ejemplo:
    from app.models.user import User, Role  # noqa: F401
"""
