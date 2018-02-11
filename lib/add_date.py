import os


def get_date(time):
    def date_formatter(date_element):
        if (date_element < 10):
            return ("0" + str(date_element))
        return str(date_element)

    day = date_formatter(time.day)
    month = date_formatter(time.month)
    year = date_formatter(time.year)
    date = "[" + year + "." + month + "." + day + "]"
    return date


## Not used yet.
##-----------------------------
def include_date(src_file):
    # Check if file name already includes a date.
    return False


def get_old_date(src_file):
    # Construct date based on old date.
    return "[yyyy.mm.dd]"


def make_new_date(old_date):
    new_date = "["
    return new_date


def date_format_yyyy_mm_dd():
    pass
##-----------------------------

def add_date(src_file, date):
    separated_file_name = src_file.split('.')
    #for i in range(len(separated_file_name)):
    #    print(separated_file_name[i])

    ext = separated_file_name[-1]
    del separated_file_name[-1]
    new_file = '.'.join(separated_file_name) + ' ' + date + '.' + ext
    return new_file


def rename_file(src_file, new_file):
    os.rename(src_file, new_file)


def main(src_file, time):
    date = get_date(time)
    new_file = add_date(src_file, date)
    rename_file(src_file, new_file)
