#!/usr/bin/env python3

import json

def search(d, filter_red):
    sum = 0
    if type(d) == dict:
        if filter_red and 'red' in list(d.values()):
            items = []
        else:
            items = list(d.values()) + list(d.keys())
    elif type(d) == list:
        items = d
    else:
        items = [d]

    for i in items:
        if type(i) == int:
            sum += int(i)
        elif type(i) in [dict, list]:
            sum += search(i, filter_red)
    return sum


data = json.load(open('input.json'))
print('Part 1: ', search(data, False))

data = json.load(open('input.json'))
print('Part 2: ', search(data, True))

# data = json.loads('{"a":2,"b":4}')
# print(search(data))
# 
# data = json.loads('[1,2,3]')
# print(search(data))
# 
# data = json.loads('[[[3]]]')
# print(search(data))
# 
# data = json.loads('{"a":{"b":4},"c":-1}')
# print(search(data))
# 
# data = json.loads('[]')
# print(search(data))