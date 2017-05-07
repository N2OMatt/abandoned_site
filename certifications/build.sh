#!/bin/bash
################################################################################
## file   : build.sh                                                          ##
## date   : Nov 3, 2016                                                       ##
## author : n2omatt <n2o.matt@gmail.com>                                      ##
##                                                                            ##
## Create the certifications images and html pages.                           ##
## Update the index with the output of certifications.                        ##
################################################################################

mkdir -p _Output;

## Update the Certifications.
cd ./_build_stuff/MyCerts;
PULL_RESULT=$(git pull origin master | grep "Already up-to-date");
cd -

EMPTY=$(ls _Output);

if [[ -z $PULL_RESULT || -z $EMPTY ]]; then
    # Build the Certifications.
    cd ./_build_stuff/certification_scripts;
        ./generate_certifications.sh;
    cd -
fi;


