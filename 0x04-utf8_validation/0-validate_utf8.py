#!/usr/bin/python3
"""
utf 8 validation file
"""


def is_continuation(byte_string):
    """
    checks byte_string if it has a continuation header
    """
    return False

def how_big_header(byte_string):
    """
    checks how big the utf 8 character is
    """
    return False


def validUTF8(data):
    """
    checks that the data is UTF-8
    assuming number is 8 bits:
    from the leftmost:
    0: normal 1 byte ascii character
    10: continuation header.

    110: 2 byte utf 8
    1110: 3 byte utf 8
    11110: 4 byte utf 8
    if header_count is not 0:
    if num is not a continuation: return false
    else
    --header_count
    if header count is 0:
    if it is a continuation: return false
    if it is normal ascii continue
    if it is one of the aforementioned headers set header_count to it - 1
    """
    header_count = 0
    for num in data:
        if num >= 256:
            return False
        if num < 0:
            return False
        byte_string = '{0:08b}'.format(num)
        if is_continuation(byte_string):
            if header_count == 0:
                return False
            header_count -= 1
        current_header_size = how_big_header(byte_string)
        if current_header_size == -1:
            return False
        if current_header_size > 0 and header_count != 0:
            return False
        if current_header_size > 0:
            header_count = current_header_size
        if byte_string[0] == '0' and header_count != 0:
            return False
    return True
