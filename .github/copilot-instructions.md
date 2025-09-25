# Copilot Instructions for AI Coding Agents

## Project Overview
This is a Django-based web application. The main components are:
- `arab/`: Django project settings and entry points (`settings.py`, `urls.py`, `wsgi.py`, `asgi.py`).
- `arabapp/`: Main Django app containing models, views, admin, static assets, and templates.
- `db.sqlite3`: Default SQLite database for local development.

## Architecture & Data Flow
- All business logic and data models reside in `arabapp/models.py`.
- URL routing is split between `arab/urls.py` (project-level) and `arabapp/urls.py` (app-level).
- Views are implemented in `arabapp/views.py` and use Django's standard request/response cycle.
- Static files and templates are organized under `arabapp/static/` and `arabapp/templates/` respectively. Static assets follow Django's conventions but include many custom CSS/JS files for frontend customization.

## Developer Workflows
- **Run server:** `python manage.py runserver` (from project root)
- **Migrations:**
  - Create: `python manage.py makemigrations arabapp`
  - Apply: `python manage.py migrate`
- **Tests:**
  - Run: `python manage.py test arabapp`
- **Debugging:** Use Django's built-in error pages and logging. No custom debug tooling detected.

## Project-Specific Patterns
- All new features should be added to `arabapp/`.
- Static files are heavily customized; reference `arabapp/static/` for frontend changes.
- Templates are organized by page/functionality in `arabapp/templates/`.
- No REST API or external service integration detected; all logic is server-rendered.
- Database is SQLite by default; production may require configuration changes in `arab/settings.py`.

## Integration Points
- No third-party Django apps or external APIs detected in settings.
- All routing and business logic is internal to the project.

## Examples
- To add a new page:
  1. Create a template in `arabapp/templates/`
  2. Add a view in `arabapp/views.py`
  3. Map the URL in `arabapp/urls.py` and include it in `arab/urls.py`

## Key Files
- `arab/settings.py`: Project configuration
- `arabapp/models.py`: Data models
- `arabapp/views.py`: Business logic
- `arabapp/static/`: Frontend assets
- `arabapp/templates/`: HTML templates

---
_If any section is unclear or missing important project-specific details, please provide feedback to improve these instructions._
