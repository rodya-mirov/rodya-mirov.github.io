#!/usr/bin/env python3

import re


def sanitize(text):
    text = text.strip()  # remove excess white noise
    text = re.sub(
        r"([\\\"])", r"\\\1", text
    )  # escape all the quotes and escape characters, so they don't blow up our formatting
    return text


tabfile = open("tab_list.js", "w")
tabcontentfile = open("tab_content.js", "w")

names = []
titles = []

linenumber = 0

# this gets all the files we need to compile and figures out their names
# then writes out the tab_content.js file, which is just a set of links to the various subpages
namefile = open("content_list.txt", "r")
for line in namefile:
    tokens = [sanitize(x) for x in line.split()]
    if len(tokens) <= 1:
        continue

    # the first token is the id
    names = names + [tokens[0]]

    # the rest of the tokens are the name of the tab
    title = tokens[1]
    for text in tokens[2:]:
        title += " " + text
    titles = titles + [title]

    if linenumber == 0:
        tabfile.write(
            'document.write("<li class=\\"active\\"><a href=\\"#'
            + names[linenumber]
            + '\\" data-toggle=\\"tab\\">'
            + title
            + '</a></li>");'
        )
    else:
        tabfile.write(
            'document.write("<li><a href=\\"#'
            + names[linenumber]
            + '\\" data-toggle=\\"tab\\">'
            + title
            + '</a></li>");'
        )

    tabcontentfile.write(
        'document.write("<script src=\\"content/'
        + names[linenumber]
        + '.js\\"></script>");'
    )

    linenumber += 1

namefile.close()
tabfile.close()
tabcontentfile.close()

linenumber = 0

# this takes a raw html file and "compiles" it to a compatible .js file
# which is essentially the bootstrap boilerplate on top, and the rest of the file
# as a big document.write( [original content, escaped properly and renamed to avoid clashes ] )
for index in range(0, len(names)):
    filename = names[
        index
    ]  # for comment purposes, assume filename is "file" (sans quotes)

    print('\tCompiling "' + filename + '"')
    input = open(filename + ".html", "r")  # we compile file.html ...
    output = open(filename + ".js", "w")  # ...into file.js

    if linenumber == 0:  # first line in the tab list is "active," while others are not
        text = '<div class=\\"tab-pane active fade in\\" id=\\"' + filename + '\\">'
    else:
        text = '<div class=\\"tab-pane fade\\" id=\\"' + filename + '\\">'

    for line in input:
        line = line.strip()

        line = re.sub(
            r"id=\"(.*)\"", 'id="' + filename + r"\1" + '"', line
        )  # id="blerg" -> id="fileblerg"
        line = re.sub(
            r"id=\'(.*)\'", "id='" + filename + r"\1" + "'", line
        )  # id='blerg' -> id='fileblerg'

        line = re.sub(
            r"showdiv\(\"(.*)\"\)", 'showdiv("' + filename + r"\1" + '")', line
        )  # showdiv("blerg") -> showdiv("fileblerg")
        line = re.sub(
            r"showdiv\(\'(.*)\'\)", "showdiv('" + filename + r"\1" + "')", line
        )  # showdiv('blerg') -> showdiv('fileblerg')

        line = sanitize(line)

        text += line
        linenumber += 1

    text += "</div>"
    output.write('document.write("' + text + '");\n')
    input.close()
    output.close()
