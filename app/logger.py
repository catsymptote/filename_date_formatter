import os
import datetime



def log(script, src_file, new_file):
    script_path = __file__
    script_dirname = os.path.dirname(script_path)
    f_name = script_dirname + '/log_file.txt'

    f = open(f_name, 'a+')
    line1 = 'script:\t\t' + str(script) + '\n'
    line2 = 'time:\t\t' + str(datetime.datetime.now()) + '\n'
    line3 = 'src_file:\t' + str(src_file) + '\n'
    line4 = 'new_file:\t' + str(new_file) + '\n'

    line = '\n' + line1 + line2 + line3 + line4
    f.write(line)
    f.close()


if __name__ == '__main__':
    log('test_script', 'file_name_1', 'file_name_2')
