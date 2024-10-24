#!/usr/bin/python3
"""
REGEX
IP: ([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]).
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]).
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]).
([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])
 - : -
Date:
year: [1-9][1-9][1-9][1-9]
month: 1[0-2] | [0-9]
TODO: doesn't account for leap years, maybe do it in code.
day: [1-2]?[0-9] | 3[0-1]
hour: (0 -> 23) 2[0-3] | [0-1]?[0-9]
minute: (0 -> 59) [0-5]?[0-9]
second: same as minute.
millisecond: [0-9] 6 times
 "GET /projects/260 HTTP/1.1" :  "GET /projects/260 HTTP/1.1"
status code: 200 | 301 | 400 | 401 | 403 | 404 | 405 | 500
filesize: [0-9] * 6
"""
import re
import signal
import sys

start = "(^"
ip_regex = (
    r'([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])'
    r'\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2['
    r'0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])')
middle = r' - '
year_regex = r'\[([0-9][0-9][0-9][0-9])-'
month_regex = r'(1[0-2]|[0-9])-'
day_regex = r'(2[0-3]|[0-1]?[0-9]) '
hour_regex = r'(2[0-3]|[0-1]?[0-9]):'
minute_regex = r'([0-5]?[0-9])'
after_minute = r':'
second_regex = minute_regex
after_second = r'\.'
before_millisecond = r'('
millisecond_regex = '[0-9]' * 6
after_millisecond = r')\] '
request_regex = r'"GET \/projects\/260 HTTP\/1.1"'
after_request = ' '
status_codes_regex = '(200|301|400|401|403|404|405|500)'
after_status = after_request
file_size_regex = '(([1-9][0-9]*)'
end = '$)'
complete = (start + ip_regex + middle + year_regex + month_regex
            + day_regex + hour_regex + minute_regex + after_minute
            + second_regex
            + after_second + before_millisecond + millisecond_regex
            + after_millisecond + request_regex
            + after_request + status_codes_regex + after_status
            + file_size_regex + end)

date_check_re = (year_regex + month_regex
                 + day_regex + hour_regex + minute_regex + after_minute
                 + second_regex
                 + after_second + before_millisecond + millisecond_regex
                 + after_millisecond)

total_size = 0
status_code_counts = {
    '200': 0,
    '301': 0,
    '400': 0,
    '401': 0,
    '403': 0,
    '404': 0,
    '405': 0,
    '500': 0
}
counter = 0


def signal_handler(sig, frame):
    """ handles signal """
    print_items()


def print_items():
    """ prints items """
    global total_size
    global status_code_counts
    print(f'File size: {total_size}')
    for key, value in status_code_counts.items():
        if value > 0:
            print(f'{key}: {value}')


def is_full_match(rematch, length):
    if not rematch:
        return False
    return rematch.start() == 0 and rematch.end() == length


if __name__ == '__main__':
    try:
        for line in sys.stdin:
            line_sections = line.split()
            if counter == 10:
                counter = 0
                print_items()

            if len(line_sections) != 9:
                continue
            counter += 1

            ip_check = re.match(ip_regex, line_sections[0])
            if not is_full_match(ip_check, len(line_sections[0])):
                continue
            if line_sections[1] != '-':
                continue
            full_date = line_sections[2] + line_sections[3]
            date_check = re.match(date_check_re, full_date)
            # if not is_full_match(date_check, len(full_date)):
            #     continue
            # if line_sections[4] != '"GET':
            #     continue
            # if line_sections[5] != '/projects/260':
            #     continue
            # if line_sections[6] != 'HTTP/1.1"':
            #     continue
            status_code = line_sections[7]

            file_size = line_sections[8]
            if file_size.isdigit():
                total_size += int(file_size)
            if status_code.isdigit():
                if status_code not in status_code_counts:
                    continue
                status_code_counts[status_code] += 1

    finally:
        print_items()
