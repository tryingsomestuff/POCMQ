kill -9 $(cat pid/celery.pid | awk '{print $NF}')
kill -9 $(cat pid/flask.pid | awk '{print $NF}')

rm */*.pid


