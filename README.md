cmdline-bookmarks
=================


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
