#!/bin/bash
##
## Author:  N2OMatt
## Date:    Dec 31 2015
## License: GPLv3
##
## This script will generate:
## 1) One page with all certifications (links) grouped by provider.
## 2) A page with the certification image and name - for each certification.
##


################################################################################
## Vars                                                                       ##
################################################################################
SITE_ROOT_PATH=$(readlink -f $PWD/../..)
SOURCE_PATH=$SITE_ROOT_PATH/_build_stuff/MyCerts


################################################################################
## Script Initialization                                                      ##
################################################################################
echo "Generating images...";
./generate_images.sh
echo "Generating mds...";
./generate_htmls.sh
echo "Generating list...";
./generate_list.sh

echo "done...";
