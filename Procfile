release: pipenv run python manage.py makemigrations && pipenv run python manage.py migrate
web: pipenv run gunicorn shop.wsgi