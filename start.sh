#!/bin/bash

mkdir -p pid

cd Celery
celery -A task worker --loglevel=info &
echo "Celery pid $!" > ../pid/celery.pid
cd -
export PYTHONPATH=$PYTHONPATH:$(readlink -f Celery)
sleep 5
cd Service
FLASK_APP=runner.py flask run --host=0.0.0.0 &
echo "Flask pid $!" > ../pid/flask.pid
cd -
sleep 5

