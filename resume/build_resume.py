#!/usr/bin/python

import os;
import sys;


def is_meta_tag(line):
    return line.startswith("__") and line.endswith("__");

def filename_from_meta_tag(tag):
    return tag.replace("__", "").lower();

def parse_file(filename):
    print "Parsing file: {0}".format(filename);

    lines_to_write = [];
    lines          = open(filename).readlines();

    for line in lines:
        clean_line = line.strip();

        if(not is_meta_tag(clean_line)):
            lines_to_write.append(line);
            continue;

        tag_filename = filename_from_meta_tag(clean_line);
        print "Found tag ({0}): {1}".format(clean_line, tag_filename);

        parsed_lines = parse_file(tag_filename + ".html");
        for parsed_line in parsed_lines:
            lines_to_write.append(parsed_line);

    return lines_to_write;


lines_to_write = parse_file("index_original.html");

f = open("result.html", "w");
f.writelines(lines_to_write);
f.close();
