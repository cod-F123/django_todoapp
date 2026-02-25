Todo App (Django)

This repository contains a simple Todo web application built with Django. It provides basic user authentication, task management, HTML templates, and static assets. The project uses SQLite by default and includes a small set of apps organized under the project root.

Quick summary
- Framework: Django (see `requirements.txt` for installed packages)
- Database: SQLite (`db.sqlite3`)
- Apps: `accounts` (auth), `todo` (task management), `core` (project settings)

Requirements
- Python 3.8 or newer
- (Recommended) Use a virtual environment for development

Environment
This project uses a local `.env` file (see `.env`) to store sensitive settings during development (e.g. `SECRET_KEY`, `DEBUG`, `ALLOWED_HOSTS`). Do NOT commit production secrets.

Setup (development)
1. Create and activate a virtual environment.

```bash
python3 -m venv venv
source venv/bin/activate
```

2. Install dependencies from `requirements.txt`.

```bash
pip install -r requirements.txt
```

3. Apply migrations and create a superuser (optional):

```bash
python manage.py migrate
python manage.py createsuperuser
```

4. Run the development server:

```bash
python manage.py runserver
```

Open http://127.0.0.1:8000/ in your browser.

Project layout (important files)
- `manage.py` — Django management script
- `db.sqlite3` — default SQLite database file (auto-created)
- `core/` — project settings & WSGI/ASGI (`core/settings.py`, `core/urls.py`)
- `accounts/` — authentication-related views, models, forms, urls
- `todo/` — todo models, views, forms, and urls
- `templates/` — HTML templates
  - `templates/accounts/login.html`
  - `templates/todo/index.html`
- `static/` — static files (CSS/JS)
- `.env` — local environment variables (development only)
- `requirements.txt` — pinned Python packages (project dependencies)
