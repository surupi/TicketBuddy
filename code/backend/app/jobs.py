#importing celery
#creating celery instance

#Celery is a distributed task queue library for Python
#commonly used to handle asynchronous and scheduled tasks in applications
#enabling efficient background processing and workload management.

from celery import Celery
celery_app = Celery(
                    backend='redis://localhost', 
                    broker="redis://localhost:6379/1",
                    broker_connection_retry_on_startup=True
                    )
    