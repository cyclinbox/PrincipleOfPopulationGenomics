#!/bin/bash
# A manually backup and deploy script for ProjectHoneyBee
# modified on 2022-11-29.

# For Windows system with Busybox, run command:
# `busybox sh manual_backup_and_deploy.sh`

cd src # change dir to `src`

# Before we get start, generate a new `index.html` file may be a great idea.
python make_indexpage.py

cd ..  # then change back

# First we need to deploy all html into `docs` directory
cp -f src/*.html docs/

# Then make backup
date=`date +%Y-%m-%d_%H%M%S`
tar -zcf backup/ProjectHoneyBee_${date}.tar.gz src/asset/ src/*.md docs/



