#!/bin/bash

set -e -x

mkdir public

python manage.py distill-local public --force
