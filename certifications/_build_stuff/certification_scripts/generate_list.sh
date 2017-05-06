#!/bin/bash
##
## Author:  N2OMatt
## Date:    Dec 31 2015
## License: GPLv3
##
## This script will scan the Certification directory and generate
## a list of certifications links.
##

################################################################################
## Vars                                                                       ##
################################################################################
SITE_ROOT_PATH=$(readlink -f $PWD/../..)
SOURCE_PATH=$SITE_ROOT_PATH/_build_stuff/MyCerts


################################################################################
## Functions                                                                  ##
################################################################################
url_encode()
{
    echo $(python -c "import sys, urllib as ul; \
    print ul.quote(\" \".join(sys.argv[1:]))" $1)
}

create_list()
{
    #Change the to the htmls directory to ease
    #the paths manipulation.
    cd $SOURCE_PATH;

    TEMP_FILENAMES_FILE=$SOURCE_PATH/temp.txt;
    OUTPUT_FILE="_Output/certs.html";


    #Save all certification filenames into temp file.
    find . -not \( -path '*/\.*' -or -path '*/_*' \)                    \
           \( -iname "*.pdf" -or -iname "*.jpg" -or -iname "*.png" \) | \
    sort > $TEMP_FILENAMES_FILE;

    cd $SITE_ROOT_PATH;
    rm -rf $OUTPUT_FILE

    CURRENT_PROVIDER_NAME="INVALID";
    while read LINE ; do
        #Get the name of provider.
        PROVIDER_NAME=$(echo $LINE | cut -d \/ -f 2);
        #Get the name of certification.
        #Remove path.
        #Remove extension.
        #Remove the date.
        CERTIFICATION_FULL_NAME=$(basename "$LINE")
        CERTIFICATION_NAME="${CERTIFICATION_FULL_NAME%.*}"

        CERTIFICATION_NAME=$(echo $CERTIFICATION_NAME | cut -d \/ -f 3     \
                                                      | cut -d _  -f 4-100 );

        #Get the name of certification (whitespaced).
        WHITESPACED_NAME=$(echo $CERTIFICATION_NAME | sed s/_/" "/g);

        #Check if the provider changed and add a header for it.
        if [ $PROVIDER_NAME != $CURRENT_PROVIDER_NAME ]; then
            if [ $CURRENT_PROVIDER_NAME != "INVALID" ]; then
                echo "<br>" >> $OUTPUT_FILE;
                echo "<br>" >> $OUTPUT_FILE;
            fi;

            echo "<b>$PROVIDER_NAME</b>" >> $OUTPUT_FILE;
            CURRENT_PROVIDER_NAME=$PROVIDER_NAME
        fi;

        ##Echo the Certification name (link).
        CERTIFICATION_URL=$(url_encode certs/$CERTIFICATION_NAME.html)
        echo "$CERTIFICATION_NAME.html"
        echo "<li><a href=\"$CERTIFICATION_URL\">$WHITESPACED_NAME</a>" >> $OUTPUT_FILE;

    done < $TEMP_FILENAMES_FILE;

    #Remove the temp file.
    rm $TEMP_FILENAMES_FILE;
}

################################################################################
## Script Initialization                                                      ##
################################################################################
create_list
