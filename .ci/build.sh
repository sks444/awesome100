#!/bin/bash

chmod +x .ci/build.sh

set -e -x

mkdir public

python manage.py distill-local public --force
