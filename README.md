# sahmino
Sahmino Backend

This is the backend for the Sahmino project, built with Django. It provides REST API endpoints for managing items, which are consumed by the Next.js frontend.

## Features
- Create new items via API
- List all items via API
- CORS enabled for frontend-backend communication

## Getting Started

### Prerequisites
- Python 3.11+
- pip

### Installation
1. Clone the repository:
	```bash
	git clone https://github.com/AliArefi1993/sahmino.git
	cd sahmino
	```
2. Install dependencies:
	```bash
	pip install -r requirements.txt
	```
3. Run migrations:
	```bash
	python manage.py migrate
	```
4. Start the development server:
	```bash
	python manage.py runserver
	```
5. API will be available at [http://localhost:8000](http://localhost:8000)

### API Endpoints
- `GET /api/items/` — List all items
- `POST /api/items/create/` — Create a new item

## Project Structure
```
sahmino/
  core/
	 models.py      # Item model
	 views.py       # API views
	 urls.py        # API routing
	 tests.py       # Tests
  sahmino/
	 settings.py    # Django settings (CORS enabled)
	 urls.py        # Project URLs
  db.sqlite3       # SQLite database
  manage.py        # Django management script
  README.md
```

## Useful Notes for Future Sessions
- API endpoints for items are in `core/views.py` and registered in `core/urls.py`.
- CORS is enabled in `sahmino/settings.py` for frontend communication.
- To add new fields to items, update `core/models.py` and run migrations.
- For frontend integration, ensure API URLs match those in the frontend code.
- For further backend features, add new views and register them in `core/urls.py`.
- For database changes, use Django migrations.

## License
MIT
