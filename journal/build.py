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

def replace_journal_index_template_contents(template, title, imgs):
    return template.replace(
        "__TEMPLATE_REPLACE_TITLE__",
         title
    ).replace(
        "__TEMPLATE_REPLACE_IMG__",
        imgs
    );


def parse_journal_entry_info(info_path):
    info_text = read_file_text(info_path).split("\n");
    info_dict = {};

    for line in info_text:
        components = line.split(":");
        if(len(components) != 2):
            continue;
        info_dict[components[0].strip(" ")] = components[1].strip(" ");

    return info_dict;

def process_journal_entry(journal_path, journal_index_template):
    print "Processing Journal Entry: {0}".format(journal_path);

    img_path  = os.path.join(journal_path, "img"     );
    info_path = os.path.join(journal_path, "info.txt");

    ## Build a list of html img tags for all
    ## images contained into the directory
    html_img_contents = "";
    img_tag_fmt = "<a href=\"img/{0}\"><img src=\"img/{0}\" width=\"50%\" height=\"50%\" ></a>\n";

    for img in sorted(os.listdir(img_path)):
        html_img_contents += img_tag_fmt.format(img);

    ## Parse the Info file
    info = parse_journal_entry_info(info_path);

    ## Replace the template with contents.
    replaced_text = replace_journal_index_template_contents(
        journal_index_template,
        info["Title"],
        html_img_contents
    );

    ## Save the index.html file.
    index_html_output_path = os.path.join(
        journal_path,
        "index.html"
    );

    write_file_text(index_html_output_path, replaced_text)

    ## Return a processed entry.
    li_fmt = "<li><b>{0}</b> - {1} - ({2})<br><a href=\"{3}\">photos</a></li>"

    entry_li = li_fmt.format(
        info["Title"],
        info["Place"],
        info["Date" ],
        os.path.join("./", journal_path, "index.html")
    );

    return entry_li

def process_journal_entries():
    entries_li = [];
    for journal_entry_path in os.listdir("."):
        if "_Output" in journal_entry_path or os.path.isdir(journal_entry_path) == False:
            continue;

        entries_li.append(
            process_journal_entry(
                journal_entry_path,
                journal_index_template
            )
        );

        ## Copy the lectures dir to _Output.
        shutil.copytree(
            journal_entry_path,
            os.path.join("_Output", journal_entry_path)
        );

    return entries_li;

################################################################################
## Script                                                                     ##
################################################################################
journal_index_template = read_file_text("journal_entry_index.template");
index_template         = read_file_text("index_original.html");

os.system("rm -rf _Output && mkdir -p _Output");

def main():
    entries = process_journal_entries();

    index_replaced = index_template.replace(
        "__TEMPLATE_REPLACE_JOURNAL_ENTRIES__",
        "".join(entries)
    );

    index_output_path = os.path.join("_Output", "index.html");
    write_file_text(index_output_path, index_replaced);

if __name__ == '__main__':
    main()






