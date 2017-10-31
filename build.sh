#!/bin/bash

SCRIPT=$(realpath -s $0);
SCRIPTPATH=$(dirname $SCRIPT);

cd $SCRIPTPATH;
git pull origin master;

mkdir -p /var/www/html/~n2omatt
./build.py /var/www/html/~n2omatt

ln -fs /var/www/html/~n2omatt /var/www/html/n2omatt
