#!/usr/bin/python3

# <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
"""
REGEX
IP: ([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])
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
# <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>
import re

test = r'238.31.240.119 - [2024-10-23 14:17:46.877469] "GET /projects/260 HTTP/1.1" 404 183'

start = "(^"
ip_regex = (r'([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2['
            r'0-4][0-9]|25[0-5])\.([01]?[0-9][0-9]?|2[0-4][0-9]|25[0-5]))')
middle = r' - '
year_regex = r'\[([0-9][0-9][0-9][0-9])-'
month_regex = '(1[0-2]|[0-9])-'
day_regex = '(2[0-3]|[0-1]?[0-9]) '
hour_regex = r'(2[0-3]|[0-1]?[0-9]):'
minute_regex = '([0-5]?[0-9])'
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
            + day_regex + hour_regex + minute_regex + after_minute + second_regex + after_second + before_millisecond + millisecond_regex
            + after_millisecond + request_regex + after_request + status_codes_regex + after_status
            + file_size_regex + end)
counter = 0
while True:
    line = input()
    x = re.match(complete, test)
    start = x.start()
    end = x.end()
    counter += 1
    if start != 0 or end != len(line):
        print(line)
        print(counter)
        print()
