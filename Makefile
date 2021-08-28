

install:
	pip install --upgrade pip
	pip install -r requirements.txt

test:
	pytest tests/test_app.py

run:
	uvicorn app:app --app-dir src