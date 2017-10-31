#!/bin/bash
##~---------------------------------------------------------------------------##
##                        ____                       _   _                    ##
##                  _ __ |___ \ ___  _ __ ___   __ _| |_| |_                  ##
##                 | '_ \  __) / _ \| '_ ` _ \ / _` | __| __|                 ##
##                 | | | |/ __/ (_) | | | | | | (_| | |_| |_                  ##
##                 |_| |_|_____\___/|_| |_| |_|\__,_|\__|\__|                 ##
##                              www.n2omatt.com                               ##
##  File      : build.sh                                                      ##
##  Project   : site                                                          ##
##  Date      : Nov 3, 2016                                                   ##
##  License   : GPLv3                                                         ##
##  Author    : n2omatt <n2omatt@amazingcow.com>                              ##
##  Copyright : n2omatt - 2017                                                ##
##                                                                            ##
##  Description :                                                             ##
##    Create the certifications images and html pages.                        ##
##    Update the index with the output of certifications.                     ##
##---------------------------------------------------------------------------~##

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)";
cd $SCRIPT_DIR;

mkdir -p _Output;

## Update the Certifications.
cd ./_build_stuff/MyCerts;
PULL_RESULT=$(git pull origin master | grep "Already up-to-date");
cd -

EMPTY=$(ls _Output/certs/certs.html);

if [[ -z $PULL_RESULT || -z $EMPTY ]]; then
    # Build the Certifications.
    cd ./_build_stuff/certification_scripts;
        ./generate_certifications.sh;
    cd -
fi;


