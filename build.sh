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
for file in `ls src/|grep html`;do
	sed -e 's/<meta charset="UTF-8">/<meta charset="UTF-8"><meta name="viewport" content="width=device-width, user-scalable=no,initial-scale=1.0,maximum-scale=1.0,minimum-scale=1.0">/g' src/${file} | 	\
	sed -e 's/<meta charset="UTF-8">/<script>var _hmt=_hmt||[];(function(){var hm=document.createElement("script");hm.src="https:\/\/hm.baidu.com\/hm.js?8fd7869a3d296e620f31f7541dec4e7f";var s=document.getElementsByTagName("script")[0];s.parentNode.insertBefore(hm,s);})();<\/script>/g' \
	> docs/${file}
done

# ...and copy `asset` directory to `docs`
cp -ruv src/asset/ docs/asset/

#cp -f src/*.html docs/

# Then make backup
date=`date +%Y-%m-%d_%H%M%S`
tar -zcf backup/ProjectHoneyBee_${date}.tar.gz src/asset/ src/*.md docs/



