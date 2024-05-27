#used to start a Celery worker process and a Celery beat process.
#Celery is a distributed task queue system for Python that allows you to run asynchronous tasks in the background.

celery -A task worker -B