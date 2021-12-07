#!/usr/bin/env python3

with open('./input.txt') as fd:
    strings = [l.strip() for l in fd]

def string_escape(s):
    ns = s
    ns = ns.replace('\\', '\\\\')
    ns = ns.replace('\"', '\\\"')
    return '"' + ns + '"'


total = 0
for s in strings:
    # s_encode = bytes(s, "utf-8").decode("unicode_escape")
    #s_encode = s.encode("raw_unicode_escape")
    s_encode = string_escape(s)
    print(s, len(s), '-> ', s_encode, len(s_encode))
    total += len(s) - len(s_encode)
print(total)
