#!/usr/bin/env python3

import re


def sanitize(text):
    text = text.strip()  # remove excess white noise
    text = re.sub(
        r"([\\\"])", r"\\\1", text
    )  # escape all the quotes and escape characters, so they don't blow up our formatting
    return text


def escape_for_js_string(text):
    """Escape a string for use inside a JavaScript string literal (double quotes)
    Note: text should already have quotes escaped by sanitize(), this handles other special chars
    """
    # Escape newlines and carriage returns (quotes and backslashes already handled by sanitize)
    text = text.replace("\n", "\\n")  # Escape newlines
    text = text.replace("\r", "\\r")  # Escape carriage returns
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
            '(function() { var parent = document.currentScript && document.currentScript.parentElement; if (parent) parent.insertAdjacentHTML("beforeend", "<li class=\\"active\\"><a href=\\"#'
            + names[linenumber]
            + '\\" data-toggle=\\"tab\\">'
            + title
            + '</a></li>"); })();'
        )
    else:
        tabfile.write(
            '(function() { var parent = document.currentScript && document.currentScript.parentElement; if (parent) parent.insertAdjacentHTML("beforeend", "<li><a href=\\"#'
            + names[linenumber]
            + '\\" data-toggle=\\"tab\\">'
            + title
            + '</a></li>"); })();'
        )

    tabcontentfile.write(
        '(function() { var container = document.currentScript && document.currentScript.parentElement; if (container) { var script = document.createElement("script"); script.src = "content/'
        + names[linenumber]
        + '.js"; container.appendChild(script); } })();'
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
    # Use DOM manipulation instead of document.write
    # Find the tab-content container and append the content
    # Escape the HTML string properly for JavaScript
    escaped_text = escape_for_js_string(text)
    output.write(
        '(function() { var container = document.querySelector(".tab-content"); if (container) container.insertAdjacentHTML("beforeend", "'
        + escaped_text
        + '"); })();\n'
    )
    input.close()
    output.close()
