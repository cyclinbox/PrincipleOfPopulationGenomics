#!/bin/bash
# A automately deploy script for ProjectHoneyBee
# modified on 2023-4-24.
# depended on `build.sh`

COMIT=`date +%Y-%m-%d`:"some edit"."$1"
./build.sh
git add *
git commit -m "$COMIT"
git push -u origin main

