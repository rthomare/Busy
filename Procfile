release: python manage.py migrate --noinput;
release: pip install -r requirements.txt
web: gunicorn App.wsgi --log-file -
release: python3 manage.py makemigrations
release: python3 manage.py migrate
release: python3 manage.py modelrefresh