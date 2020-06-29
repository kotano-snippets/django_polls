wsgi:
	export DJANGO_SETTINGS_MODULE=hello_django.settings
	gunicorn hello_django.wsgi
run:
	manage.py runserver

test:
	pytest -vv

lint:
	flake8
	pydocstyle