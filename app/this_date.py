import add_date
import sys
import datetime
import logger


def get_time_now():
    time = datetime.datetime.now()
    return time


src_file = sys.argv[1]
new_file = add_date.main(src_file, get_time_now())
logger.log('this_date', src_file, new_file)
