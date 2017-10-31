#!/bin/bash
################################################################################
## file   : build.sh                                                          ##
## date   : Nov 3, 2016                                                       ##
## author : n2omatt <n2o.matt@gmail.com>                                      ##
##                                                                            ##
## Copy the resumes to Output folder.                                         ##
################################################################################

echo "Processing Resume."
## Clean
rm    -rf ./_Output
mkdir -p  ./_Output

## Build
./build_resume.py

## Copy content
mv result.html ./_Output/index.html
