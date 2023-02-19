import os
from datetime import datetime
import types
from decorator1 import logger

@logger
def flat_generator(list_of_lists):
	for item in list_of_lists:
		for element in item:
			yield element


if __name__ == '__main__':
    list_of_lists_1 = [
        ['a', 'b', 'c'],
        ['d', 'e', 'f', 'h', False],
        [1, 2, None]
    ]

    for item in flat_generator(list_of_lists_1):
        print(item)
