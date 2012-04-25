#!/bin/bash

#The patch number is what will appear after 2.5.2-jbossorg-, e.g. 2.5.2-jbossorg-1
export JBOSS_ORG_PATCH=1
ant clean
ant full-build -Djbossorg.patch=$JBOSS_ORG_PATCH
rm -rf dist/standalone-jar
java -jar jython_installer-2.5.2.jar -s -d dist/standalone-jar -t standalone
