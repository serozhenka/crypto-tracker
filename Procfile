web: daphne config.asgi:application --port $PORT --bind 0.0.0.0 -v2
celery: celery -A config worker --beat --scheduler django  --loglevel=info
