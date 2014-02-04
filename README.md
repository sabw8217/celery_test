celery_test
===========

Celery worker hang test.

To run:
- have RabbitMQ running locally on port 5672
- from the Python shell:
> import tasks
> tasks.enqueue_tasks()

- run `celery -A tasks worker --without-gossip --without-mingle -Q celery_test`
