PYTHON = python
SRC_DIR = src
APPS_DIR = $(SRC_DIR)/apps
VENV_DIR = venv

run:
	$(PYTHON) $(SRC_DIR)/manage.py runserver

migrate:
	$(PYTHON) $(SRC_DIR)/manage.py makemigrations
	$(PYTHON) $(SRC_DIR)/manage.py migrate

superuser:
	$(PYTHON) $(SRC_DIR)/manage.py createsuperuser

app:
	$(PYTHON) $(SRC_DIR)/manage.py startapp $(name)
	mv $(name) $(SRC_DIR)

requirements:
	pip freeze > requirements.txt
