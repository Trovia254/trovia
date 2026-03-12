web: python manage.py migrate --settings=trovia.settings.prod && python manage.py collectstatic --noinput --settings=trovia.settings.prod && gunicorn trovia.wsgi:application --bind 0.0.0.0:$PORT
