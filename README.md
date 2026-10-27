# Gestión de proyectos de software

Aplicación web modular para administrar y dar seguimiento a proyectos de software.
Stack: **Flask · SQLAlchemy · SQLite (dev) · Bootstrap 5**.

## Integrantes
| Nombre | Rol inicial |
|---|---|
| _Integrante 1_ | A: Backend y seguridad |
| _Integrante 2_ | B: Base de datos y datos |
| _Integrante 3_ | C: Frontend e integración |

## Puesta en marcha

```bash
git clone <URL-DEL-REPO>
cd proyecto-gestion

python -m venv venv
# Windows:  venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

pip install -r requirements.txt
cp .env.example .env        # Windows: copy .env.example .env

flask db init               # solo la primera vez (si no existe migrations/)
flask db migrate -m "estado inicial"
flask db upgrade
flask run
```

Abre http://127.0.0.1:5000. La ruta `/salud` responde `{"estado": "ok"}`.

## Estructura

```
app/
├── __init__.py      # create_app(): extensiones y blueprints
├── extensions.py    # db, migrate, login_manager, csrf, bcrypt
├── models/          # un archivo por entidad
├── main/            # inicio y /salud
├── auth/            # Hito 1: registro, login, recuperación
├── users/           # Hito 1: CRUD de usuarios
├── projects/        # Hito 2: proyectos, miembros, fases
├── tasks/           # Hito 3: tareas, horas, Kanban
├── risks/           # Hito 4: riesgos y documentación
├── dashboard/       # Hito 5: métricas e informe PDF
├── templates/
└── static/
config.py · run.py · requirements.txt
```

## Flujo de Git

- `main`: siempre estable. `develop`: integración.
- Una rama por parte del plan: `feature/1.3-auth-basica`.
- Todo entra por Pull Request revisado por otro integrante.
- Al cerrar un hito: merge a `main` y tag (`v0.1-hito1`, `v0.2-hito2`...).
- Commits descriptivos: `feat(auth): agrega recuperación de contraseña`.

## Avance por hitos

- [ ] Hito 1: Usuarios, roles y autenticación
- [ ] Hito 2: Proyectos y fases
- [ ] Hito 3: Tareas y estimación
- [ ] Hito 4: Riesgos y documentación
- [ ] Hito 5: Dashboard, informe PDF y despliegue
