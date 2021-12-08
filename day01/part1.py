#!/usr/bin/env python3

with open('./test.txt') as fd:
	items = [x.strip() for x in fd]

print(items)

for i in items:
	print(i.count('(') - i.count(')'))
