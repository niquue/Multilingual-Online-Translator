# Multilingual-Online-Translator
This is a multilingual online translator that uses HTML and Python to web-scrape from an online translator website.

The user is able to choose from a list of 13 languages to translate to and from. They also able to input a word they wish to translate. 
- As an example, the user could enter: English, French, "Hello" and this program will translate the word "Hello" from English to French,
and display the output to the user with a few word translations as well as example sentences.

The command line is also made of use if the user wishes to use the command line to quickly input their entries.
Each time the user enters an entry, a TEXT(.txt) document is created on their machine of the outputs with the file name of:
{word inputted to translate}.txt. ie: hello.txt, hola.txt, hi.txt

This project was also a lesson on use of BeautifulSoup, HTML parsers, XML, scraping, and use of the argparse module / library

# BeautifulSoup
- Beautiful Soup is a Python package for parsing HTML and XML documents (including having malformed markup, i.e. non-closed tags, so named after tag soup). It creates a parse tree for parsed pages that can be used to extract data from HTML,[2] which is useful for web scraping.[1]

Beautiful Soup was started by Leonard Richardson, who continues to contribute to the project,[3] and is additionally supported by Tidelift, a paid subscription to open-source maintenance.[4]

It is available for Python 2.7 and Python 3
(Source: https://en.wikipedia.org/wiki/Beautiful_Soup_(HTML_parser))

# XML
- Extensible Markup Language (XML) is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable. The World Wide Web Consortium's XML 1.0 Specification[2] of 1998[3] and several other related specifications[4]—all of them free open standards—define XML.[5] 
Source(https://en.wikipedia.org/wiki/XML)

# argparse
- The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages and issues errors when users give the program invalid arguments
Source(https://docs.python.org/3/library/argparse.html)

