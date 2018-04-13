#!/bin/bash

chmod +x .ci/build.sh

set -e -x

mkdir _site public

python manage.py collectstatic --noinput
python manage.py distill-local public --force
