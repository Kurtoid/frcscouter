release: python manage.py migrate --noinput
web: gunicorn scouter.wsgi --log-file=- --log-level=debug
log: tail -f scouter.log
