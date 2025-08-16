# Sahmino Backend Documentation

This directory contains documentation for the Django backend project.

## Structure
- `core/`: Main app containing models, views, URLs, and admin configuration.
- `sahmino/`: Project settings, URLs, and WSGI/ASGI entry points.

## Getting Started
1. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
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
