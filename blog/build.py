#!/usr/bin/python
################################################################################
## File   : build.py                                                          ##
## Author : n2omatt - n2omatt@amazingcow.com                                  ##
## Date   : May 2, 2017                                                       ##
##                                                                            ##
## Description:                                                               ##
##   Generates an full html page with the content of each blog entry.         ##
##   All blog entries are just the "inner" content, i.e without the body      ##
##   headers etc. that are need to be a valid html page.                      ##
##   So this script will create the valid pages and generate an listing of    ##
##   the last X entries to be inserted on the index.html.                     ##
################################################################################

################################################################################
## Imports                                                                    ##
################################################################################
import sys;
import os;
import os.path;


################################################################################
## Globals                                                                    ##
################################################################################
months_list = ["jan", "feb", "mar",
               "apr", "may", "jun",
               "jul", "aug", "sep",
               "oct", "nov", "dec"];

kLastEnties_Count = 5;


################################################################################
## Functions                                                                  ##
################################################################################
def get_date_from_filename(filename):
    components = filename.split("_")[0:3]; ##month_day_year_...
    return [
        months_list.index(components[0]),
        int(components[1]),
        int(components[2])
    ];

def get_title_from_file(filename):
    f = open(filename);

    ## <!-- Some catchy title... -->
    original_line = f.readline()
    clean_line    = original_line.replace("<!--", "").replace("-->", "").strip  (" ");

    f.close(); ## Closing here because we can raise ahead.

    ## Cannot clean up the line.
    ##   This means that we have a bad formatted line here.
    if(len(original_line) == len(clean_line)):
        raise Exception("Invalid title on file: ({0})".format(filename));

    return clean_line;


def find_all_blog_entries_names(start_path):
    return filter(
        lambda fn: os.path.splitext(fn)[1] == ".html",
        os.listdir(start_path)
    );

def read_file_text(filename):
    entry_file = open(filename);
    all_lines  = entry_file.readlines();

    entry_file.close();

    return "".join(all_lines);

def write_file_text(blog_entry_fullpath, text):
    outfile  = open(blog_entry_fullpath, "w");

    outfile.write(text);
    outfile.close();


def replace_blog_entry_template_contents(template, entry, title, date):
    formated_date = "{0} {1}, {2}".format(
        months_list[date[0]].capitalize(), date[1], date[2]
    );

    title_date = "<p><center><h1>{0}</h1>{1}</center></p>".format(
        title,
        formated_date
    );

    return template.replace(
        "__TEMPLATE_REPLACE_BLOG_ENTRY_CONTENTS__",
         entry
    ).replace(
        "__TEMPLATE_REPLACE_TITLE_AND_DATE__",
        title_date
    );

def replace_index_template_contents(template, text):
    return template.replace(
        "__TEMPLATE_REPLACE_BLOG_LISTING__",
         text
    );


################################################################################
## Script                                                                     ##
################################################################################
def main():
    base_dir   = "entries";
    output_dir = "_Output";

    os.system("mkdir -p {0}".format(output_dir));

    ## Replace the Blog Template with the contents for each blog entry
    ## found in the entries directory. Additionally create a index.html
    ## with the listings of each blog entry.
    blog_entry_template = read_file_text("blog_entry_template.template");
    all_blog_entries    = find_all_blog_entries_names(base_dir);

    index_template     = read_file_text("index.template");
    index_listing_dict = {};
    last_entries       = [];


    for filename in all_blog_entries:
        print "Processing Blog: {0}".format(filename);

        blog_entry_fullpath = os.path.join(base_dir, filename);

        date            = get_date_from_filename(filename);
        title           = get_title_from_file   (blog_entry_fullpath);
        blog_entry_text = read_file_text        (blog_entry_fullpath);

        ## Create the Blog Entry file.
        replaced_entry = replace_blog_entry_template_contents(
            blog_entry_template,
            blog_entry_text,
            title,
            date
        );

        blog_entry_fullpath = os.path.join(output_dir, filename);
        write_file_text(blog_entry_fullpath, replaced_entry);

        ## Add to Index listing.
        ##  We don't have this year yet, so add them to dict.
        year = date[2];
        if(not index_listing_dict.has_key(year)):
            index_listing_dict[year] = {};

        ##  We don't have this month on this year yet, so add them to dict.
        month = date[0];
        if(not index_listing_dict[year].has_key(month)):
            index_listing_dict[year][month] = [];

        index_listing_dict[year][month].append(
            { "title" : title, "url" : filename }
        );

    ## Create the index.html file
    index_list_text = "";
    for year in sorted(index_listing_dict.keys(), reverse=True):
        index_list_text += "<h2>{0}</h2>\n".format(year);

        month_dict = index_listing_dict[year];
        for month in sorted(month_dict.keys(), reverse=True):
            index_list_text += "<h3>{0}<h3>\n".format(months_list[month].capitalize());
            index_list_text += "<ul>\n";

            entries_list = month_dict[month];
            for entry in entries_list:
                index_list_text += "<li><a href=\"{0}\">{1}</a></li>\n".format(
                    entry["url"  ].replace("\n",""),
                    entry["title"].replace("\n","")
                );

                ## Here we produce the last entries need to the
                ## site main page.
                if(len(last_entries) < kLastEnties_Count):
                    entry_text = "<li><a href=\"{0}\">{1}</a></li>\n".format(
                        entry["url"  ].replace("\n",""),
                        entry["title"].replace("\n","")
                    );
                    last_entries.append(entry_text);

            index_list_text += "</ul>\n"

    ## Write to file.
    index_replaced_text = replace_index_template_contents(
        index_template,
        index_list_text
    );

    index_list_output_path = os.path.join(output_dir, "index.html");
    write_file_text(index_list_output_path, index_replaced_text);

    ## Write the Last entries file.
    last_entries_output_path = os.path.join(output_dir, "last_entries.txt");
    write_file_text(last_entries_output_path, "".join(last_entries));

if __name__ == '__main__':
    main();
