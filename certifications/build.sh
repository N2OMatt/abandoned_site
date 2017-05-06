#!/bin/bash
################################################################################
## file   : build.sh                                                          ##
## date   : Nov 3, 2016                                                       ##
## author : n2omatt <n2o.matt@gmail.com>                                      ##
##                                                                            ##
## Create the certifications images and html pages.                           ##
## Update the index with the output of certifications.                        ##
################################################################################

rm    -rf _Output;
mkdir -p  _Output;

## Update the Certifications.
cd ./_build_stuff/MyCerts;
    git pull origin master
cd -

# Build the Certifications.
cd ./_build_stuff/certification_scripts;
    ./generate_certifications.sh;
cd -


