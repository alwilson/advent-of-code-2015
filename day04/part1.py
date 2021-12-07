#!/usr/bin/env python3

import hashlib
import sys

i = 0
while True:
    hash_str = sys.argv[1] + str(i)
    md5hash = hashlib.md5(hash_str.encode('utf-8'))
    # print(hash_str, '-', md5hash.hexdigest())
    if md5hash.hexdigest()[0:6] == '000000':
        print(hash_str, '-', md5hash.hexdigest())
        print(i)
        break
    if md5hash.hexdigest()[0:5] == '00000':
        print(hash_str, '-', md5hash.hexdigest())
        print(i)
    i += 1
