from celery import Celery
from celery import Task
from flask import current_app as app
from main import app as flask_app
 
#integrate Celery with Flask by creating a subclass of Celery's Task class that ensures tasks are executed within the Flask context. 
#configures a Celery instance using Redis as the backend and broker, and associates it with the Flask app.

def make_celery(app):
    class FlaskTask(Task):
        def __call__(self, *args: object, **kwargs: object) -> object:
            with app.app_context():
                return self.run(*args, **kwargs)
    
    celery_app = Celery(app.name, task_cls=FlaskTask,
                        backend='redis://localhost', 
                        broker="redis://localhost:6379/1",
                        broker_connection_retry_on_startup=True
                        )
    
    app.extensions["celery"] = celery_app
    return celery_app


celery_app = make_celery(flask_app)

