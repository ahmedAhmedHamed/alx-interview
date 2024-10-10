#!/usr/bin/python3
"""solution for lockboxes"""


def canUnlockAll(boxes):
    """solution for lockboxes"""
    keys = []
    visited = set()
    count = len(boxes) - 1
    visited.add(0)
    if len(boxes) <= 1:
        return True
    if len(boxes[0]) == 0:
        return False
    for key in boxes[0]:
        keys.append(key)
    while keys:
        current = keys.pop()
        if current < len(boxes) and current not in visited:
            visited.add(current)
            count -= 1
            for key in boxes[current]:
                keys.append(key)
        if count == 0:
            return True
    if count == 0:
        return True
    return False
