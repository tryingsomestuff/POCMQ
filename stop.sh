kill -9 $(cat Celery/celery.pid | awk '{print $NF}')
kill -9 $(cat Service/flask.pid | awk '{print $NF}')

rm */*.pid


