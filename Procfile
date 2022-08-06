web: daphne config.asgi:application --port 8888 --bind 0.0.0.0 -v2
celery: celery -A config worker --loglevel=info
beat: celery -A config beat --loglevel=info