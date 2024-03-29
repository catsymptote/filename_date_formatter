import os
import re



def date_formatter(date_element):
    """Format the date."""
    if (date_element < 10):
        return ("0" + str(date_element))
    return str(date_element)


def get_date(time):
    """Gets the date and returns the formatted date as [yyyy.mm.dd]."""
    day = date_formatter(time.day)
    month = date_formatter(time.month)
    year = date_formatter(time.year)
    date = "[" + year + "-" + month + "-" + day + "]"
    return date


## Not used yet.
##-----------------------------
## Date formats:
## 1    [yyyy-mm-dd] (default)
## 2    [yyyy.mm.dd] (old default)
## 3    [dd.mm.yyyy]
## 4    (dd.mm.yyyy)
## 5    (yyyy.mm.dd)


def existing_date(src_file):
    return False
    # Includes two brackets.
    # Has a specific format, based on brackets, dots, numbers, and other characters.

    bracketed_substrings = get_bracketed_parts(src_file)

    #if not bracketed_substrings:
    #    return False

    formats = [
        re.compile(''),
        re.compile(''),
        re.compile(''),
        re.compile('')
    ]


    format_index = 0
    while(format_index < len(formats)):
        #while(index < (len(src_file) - len(formats[format_index]))):
        tmp = re.search(formats[format_index], src_file)

    return False


## Assuming date is encapsulated in brackets.
def get_bracketed_parts(s):
    bracketed_substrings = []
    index = 0
    start_bracket = ['(', '[', '{']
    end_bracket = [')', ']', '}']
    while(index < len(s)):
        bracket_found = False
        start = 0
        end = 0
        if(s[index] in start_bracket):
            start = index
            bracket_found = True
        if(s[index] in end_bracket):
            end = index
            bracket_found = True
        if(bracket_found):
            bracketed_substrings.append(s[start:end])
    return bracketed_substrings


def get_old_date(src_file):
    """Not much functionality here."""
    # Construct date based on old date.
    return "[yyyy-mm-dd]"


def make_new_date(old_date):
    """What does this even do?"""
    new_date = "["
    return new_date


def date_format_yyyy_mm_dd():
    pass
##-----------------------------


def add_date(src_path, date):
    """Add the date to the file name."""
    if os.path.isdir(src_path):
        new_path = src_path + ' ' + date
        return new_path
    
    separated_file_name = src_path.split('.')
    ext = separated_file_name[-1]
    del separated_file_name[-1]
    new_path = '.'.join(separated_file_name) + ' ' + date + '.' + ext
    return new_path

    
    #for i in range(len(separated_file_name)):
    #    print(separated_file_name[i])

    


def rename_file(src_file, new_file):
    """Rename the src_file --> new_file."""
    os.rename(src_file, new_file)


def main(src_file, time):
    ## If existing date exists, date = existing_date. If not, date = False.
    date = existing_date(src_file)

    # If existing date:
    if date:
        new_file = make_new_date(date)
    else:
        date = get_date(time)
        new_file = add_date(src_file, date)


    rename_file(src_file, new_file)
    return new_file
