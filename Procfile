release: python manage.py makemigrations --noinput;
release: python manage.py migrate --noinput;
release: python manage.py modelrefresh;
release: pip install -r requirements.txt
web: gunicorn App.wsgi --log-file -