import sqlite3
from optparse import OptionParser
import logging
import warnings

LOG_FILENAME="bmarks.log"

db_file = "bmarks.db"
db = sqlite3.connect(db_file)
cur = db.cursor()

logging.basicConfig(level=logging.DEBUG,
    format='[%(levelname)s] (%(threadName)-10s) %(asctime)s %(message)s',
    filename = LOG_FILENAME,
    filemode='w',
    )


def create_table():
    bmarks_cmd="(url varchar(1000) NOT NULL, tag varchar(1000) NOT NULL)"
    bmarks_cmd_to_run = "CREATE TABLE IF NOT EXISTS `bmarks` "+bmarks_cmd

    warnings.filterwarnings('error')

    try:
        cur.execute(bmarks_cmd_to_run)
    except Warning:
        pass

def fetch_tag_list(list_tag):
    fetch_cmd = "select url from bmarks where tag like '%"+list_tag+"%'"
    logging.debug(fetch_cmd)

    try:
        cur.execute(fetch_cmd)
        data = cur.fetchall()
        for i in xrange(len(data)):
            print str(data[i][0])
    except:
        pass


def add_data_to_db(url, tag):
    values = " ( '%s', '%s' )" % (url, tag)
    insert_cmd = "INSERT INTO bmarks (url, tag) VALUES "+values
    logging.debug(insert_cmd)
    cur.execute(insert_cmd)
    db.commit()


if __name__ == '__main__':
    parser = OptionParser(usage="usage: %prog [options] filename",
                    version="%prog 0.1")
    parser.add_option("-u", "--url", dest="url", default='url', help="url to bookmark")
    parser.add_option("-t", "--tag", dest="tag", default='tag', help="tags for the given url")
    parser.add_option("-l", "--list", dest="list_tag", default='random_list', help="list all the urls matching specific tag")
    (options, args) = parser.parse_args()

    url = options.url
    tag = options.tag
    list_tag = options.list_tag

    logging.debug("url to bookmark : %s, tag for the url : %s " % (url, tag))
    create_table()

    if(list_tag != 'random_list'):
        fetch_tag_list(list_tag)
    if (url!='url' and tag !='tag'):
        add_data_to_db(url, tag)

