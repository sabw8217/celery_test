#!/bin/bash

virtualenv celery_test
source celery_test/bin/activate

pip install -r requirements.txt

python tasks.py
celery -A tasks worker --without-gossip --without-mingle -Q celery_test
