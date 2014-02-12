#!/bin/bash

# this script requires that you are not currently in a virtualenv
# and have an up-to-date setuptools installed.

virtualenv celery_test
source celery_test/bin/activate

pip install -r requirements.txt

python tasks.py
celery -A tasks worker --without-gossip --without-mingle -Q celery_test
