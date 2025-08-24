# Sahmino Backend Documentation

This directory contains documentation for the Django backend project.

## Structure
- `core/`: Main app containing models, views, URLs, and admin configuration.
- `sahmino/`: Project settings, URLs, and WSGI/ASGI entry points.

## Getting Started

You can use either a traditional `requirements.txt` workflow or the modern `pyproject.toml` (Poetry) workflow.

1. Using requirements.txt:
   ```bash
   pip install -r requirements.txt
   ```

2. Using Poetry / pyproject.toml:
   ```bash
   # Install Poetry (if not installed)
   curl -sSL https://install.python-poetry.org | python3 -

   # Install dependencies and create virtual environment
   poetry install

   # Activate the venv (or use `poetry run` to run commands)
   poetry shell
   python manage.py migrate
   python manage.py runserver
   ```
2. **Run migrations:**
   ```bash
   python manage.py migrate
   ```
3. **Start development server:**
   ```bash
   python manage.py runserver
   ```

## API Endpoints
- `/api/items/`: List all items (GET)
- `/api/items/create/`: Create a single item (POST)
- `/api/items/create_batch/`: Create multiple items (POST)

## Models
See `core/models.py` for model definitions.

## Contributing
- Follow PEP8 style guidelines.
- Write tests in `core/tests.py`.

## License
MIT
