import sys
import os.path


def get_output_path(file_path):
    dir = os.path.dirname(file_path)
    file = os.path.basename(file_path)
    return os.path.join(dir, '.__' + file)


def check_bytes_empty(bytes_var):
    value = int.from_bytes(bytes_var, 'big')
    return value == 0


def read_origin_file_header(file_path):
    f = open(file_path, 'rb')
    d = f.read(20)
    f.close()
    return d


def output_header(header_bytes, file_path):
    out_file = get_output_path(file_path)
    f = open(out_file, 'wb')
    f.write(header_bytes)
    f.close()


def overwrite_origin_file(file_path):
    f = open(file_path, 'r+b')
    empty_bytes = bytes(bytearray(20))
    f.write(empty_bytes)
    f.close()


def check_file(file_path):
    if not os.path.isfile(file_path):
        raise Exception('origin file not exists: ' + file_path)


if __name__ == '__main__':
    file_path = sys.argv[1]
    check_file(file_path)
    header_bytes = read_origin_file_header(file_path)
    if check_bytes_empty(header_bytes):
        raise Exception('origin file header is empty!!')
    output_header(header_bytes, file_path)
    overwrite_origin_file(file_path)
