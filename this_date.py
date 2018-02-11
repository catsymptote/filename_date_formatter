from lib import add_date
import sys
import datetime


def get_time_now():
    time = datetime.datetime.now()
    return time


src_file = sys.argv[1]
add_date.main(src_file, get_time_now())
