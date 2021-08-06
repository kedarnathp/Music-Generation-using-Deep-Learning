import collections
import pprint

with open('input.txt','r') as info:
	count = collections.Counter(info.read())
	value = pprint.pformat(count)
print(value)