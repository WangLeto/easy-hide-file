import sys
import os
from hide import get_output_path


def read_header_bytes(file_path):
    output_file = get_output_path(file_path)
    if not os.path.isfile(output_file):
        raise Exception('output_file not exist! ' + output_file)
    f = open(output_file, 'rb')
    d = f.read(20)
    f.close()
    return d


def recover_origin_file(file_path, data_bytes):
    if not os.path.isfile(file_path):
        raise Exception('origin file not exists: ' + file_path)
    f = open(file_path, 'r+b')
    f.write(data_bytes)
    f.close()


def remove_header_file(file_path):
    header_file = get_output_path(file_path)
    os.remove(header_file)


if __name__ == '__main__':
    file_path = sys.argv[1]
    data = read_header_bytes(file_path)
    recover_origin_file(file_path, data)
    remove_header_file(file_path)
