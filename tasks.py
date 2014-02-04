"""
Celery worker hang test.

To run:
- have RabbitMQ running locally on port 5672
- from the Python shell:
> import tasks
> tasks.enqueue_tasks()

- run `celery -A tasks --without-gossip --without-mingle -Q celery_test`

"""
from celery import Celery

app = Celery('tasks', broker='amqp://localhost:5672/')

@app.task
def add(x, y):
    return x + y

def enqueue_tasks():
    for i in xrange(1000):
        add.apply_async(args=(i,i),queue='celery_test')