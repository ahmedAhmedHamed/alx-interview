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
filesize: [1-9][0-9]*
"""
import datetime
print(datetime.datetime.now())
