cmdline-bookmarks
=================

$ python bmarks.py -h
Usage: bmarks.py [options] filename

Options:
  --version             show program's version number and exit
  -h, --help            show this help message and exit
  -u URL, --url=URL     url to bookmark
  -t TAG, --tag=TAG     tags for the given url
  -l LIST_TAG, --list=LIST_TAG
                        list all the urls matching specific tag


To add a new url and tag
=========================
$ python bmarks.py -u "http://bing.com" -t "search, microsoft"


To search for urls mataching a tag
===================================
$ python bmarks.py -l search
http://bing.com
http://google.com

To add a url and tag + search for urls matching a tag
======================================================
$ python bmarks.py -u "http://bing.com" -t "search, microsoft" -l search
http://bing.com
http://bing.com
http://google.com
