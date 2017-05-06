#!/usr/bin/python
################################################################################
## file   : build.py                                                          ##
## date   : May 6, 2017                                                       ##
## author : n2omatt <n2o.matt@gmail.com>                                      ##
##                                                                            ##
## Build the index.html for each lecture and                                  ##
## Copy the lectures stuff to _Output folder.                                 ##
################################################################################

################################################################################
## Imports                                                                    ##
################################################################################
import os;
import os.path;
import shutil;

################################################################################
## Functions                                                                  ##
################################################################################
def read_file_text(filename):
    entry_file = open(filename);
    all_lines  = entry_file.readlines();

    entry_file.close();

    return "".join(all_lines);

def write_file_text(blog_entry_fullpath, text):
    outfile  = open(blog_entry_fullpath, "w");

    outfile.write(text);
    outfile.close();

def replace_index_template_contents(template, text, title):
    return template.replace(
        "__TEMPLATE_REPLACE_BLOG_LISTING__",
         text
    ).replace(
        "__TEMPLATE_REPLACE_TITLE__",
        title
    );


################################################################################
## Script                                                                     ##
################################################################################
index_template = read_file_text("index.template");

os.system("rm -rf _Output && mkdir -p _Output");

for lecture_path in os.listdir("."):
    if "_Output" in lecture_path or os.path.isdir(lecture_path) == False:
        continue;

    print "Processing Lecture: {0}".format(lecture_path);


    img_path = os.path.join(lecture_path, "img");

    ## Build a list of html img tags for all
    ## images contained into the directory
    html_img_contents = "";
    img_tag_fmt = "<a href=\"img/{0}\"><img src=\"img/{0}\" width=\"25%\" height=\"25%\" ></a>\n";

    for img in sorted(os.listdir(img_path)):
        html_img_contents += img_tag_fmt.format(img);

    ## Build the title from the dir name.
    title = " ".join(
        map(lambda x: x[0].upper() + x[1:], lecture_path.split("_"))
    );

    ## Replace the template with the contents
    replaced_text = replace_index_template_contents(
        index_template,
        html_img_contents,
        title
    );

    ## Save the index.html file.
    index_html_output_path = os.path.join(
        lecture_path,
        "index.html"
    );

    write_file_text(index_html_output_path, replaced_text);

    ## Copy the lectures dir to _Output.
    shutil.copytree(
        lecture_path,
        os.path.join("_Output", lecture_path)
    );

