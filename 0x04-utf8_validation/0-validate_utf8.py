#!/usr/bin/python3
"""
utf 8 validation file
"""


def is_continuation(byte_string):
    """
    checks byte_string if it has a continuation header
    """
    return byte_string[0] == '1' and byte_string[1] == '0'


def how_big_header(byte_string):
    """
    checks how big the utf 8 character is
    """
    counter = 0
    for byte in byte_string:
        if byte != '0':
            counter += 1
        else:
            break
        if counter > 4:
            return -1
    if counter == 0:
        return counter
    return counter - 1


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
        byte_string = '{0:08b}'.format(num)
        byte_string = byte_string[-8:]
        current_header_size = how_big_header(byte_string)
        if is_continuation(byte_string):
            if header_count == 0:
                return False
            header_count -= 1
        if current_header_size == -1:
            return False
        if current_header_size > 0 and header_count != 0:
            return False
        if current_header_size > 0:
            header_count = current_header_size
        if byte_string[0] == '0' and header_count != 0:
            return False
    return header_count == 0
