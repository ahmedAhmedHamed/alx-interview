#!/usr/bin/python3
""" making change module """


def makeChange(coins, total):
	"""
	gives change given coins and total
	"""
	if total <= 0:
		return 0
	ret = 0
	if not coins:
		return -1
	coins.sort(reverse=True)
	for denomination in coins:
		temp_total = total
		ret += total // denomination
		total = total % denomination
	if total:
		return -1
	return ret
