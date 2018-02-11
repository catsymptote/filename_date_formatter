from lib import add_date
import sys
import datetime
import os


def get_mod_time(src_file):
    #time = datetime.datetime.fromtimestamp(os.path.getmtime(src_file)).strftime('%Y-%m-%d %H:%M:%S.%f')
    #time = datetime.datetime.fromtimestamp(os.path.getmtime(src_file)/1000.0)
    time = datetime.datetime.fromtimestamp(os.path.getmtime(src_file))
    return time


src_file = sys.argv[1]
add_date.main(src_file, get_mod_time(src_file))
