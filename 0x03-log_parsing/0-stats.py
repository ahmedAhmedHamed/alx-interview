#!/usr/bin/python3
"""
log parsing interview question
"""
import sys

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


def print_items():
    """ prints items """
    global total_size
    global status_code_counts
    print(f'File size: {total_size}')
    for key, value in status_code_counts.items():
        if value > 0:
            print(f'{key}: {value}')


if __name__ == '__main__':
    """
    entrypoint of program
    """
    try:
        for line in sys.stdin:
            line_sections = line.split()

            if len(line_sections) < 2:
                continue
            counter += 1

            status_code = line_sections[7]

            file_size = line_sections[8]
            total_size += int(file_size)
            if status_code.isdigit():
                if status_code in status_code_counts:
                    status_code_counts[status_code] += 1
            if counter == 10:
                counter = 0
                print_items()

    finally:
        print_items()
