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

## Copy content
cp index_original.html ./_Output/index.html
