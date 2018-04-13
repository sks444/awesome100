#!/bin/bash

chmod +x .ci/build.sh

set -e -x

mkdir _site public

python manage.py migrate
python manage.py import_best_actors
python manage.py collectstatic --noinput
python manage.py distill-local public --force
