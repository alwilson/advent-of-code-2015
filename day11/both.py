#!/usr/bin/env python3

def check_passwd(passwd, debug):
    if debug: print(f'{passwd = }: ', end='')
    result = True

    run = 2
    for c_i, c in enumerate(passwd[1:]):
        if ord(c) == ord(passwd[c_i]) + 1:
            run -= 1
            if run == 0:
                break
        else:
            run = 2
    if run != 0:
        if debug: print('no run detected, ', end='')
        result = False

    pairs = 2
    prev_pair = ''
    for c_i, c in enumerate(passwd[1:]):
        if ord(c) == ord(passwd[c_i]) and c != prev_pair:
            pairs -= 1
            prev_pair = c
            if pairs == 0:
                break
    if pairs != 0:
        if debug: print(f'{2-pairs} pairs detected, need 2 diff pairs, ', end='')
        result = False

    if 'i' in passwd or 'o' in passwd or 'l' in passwd:
        if debug: print('iol are not allowed, ', end='')
        result = False

    if debug:
        print('pass') if result else print('fail') 
    return result

def inc_pw(passwd):
    new_passwd = ''

    carry = True
    for c in passwd[::-1]:
        c_ord = ord(c)

        if c in 'iol':
            new_passwd = 'a' * len(new_passwd)
            carry = True

        if carry:
            if c_ord == ord('z'):
                new_passwd += 'a'
            else:
                new_passwd += chr(c_ord + 1)
                carry = False
        else:
            new_passwd += c
    if carry:
        new_passwd += 'a'

    return new_passwd[::-1]

def next_passwd(passwd):
    save_pw = passwd
    check_passwd(passwd, False)
    passwd = inc_pw(passwd)

    while not check_passwd(passwd, False):
        passwd = inc_pw(passwd)

    check_passwd(passwd, False)
    print(f'{save_pw} -> {passwd}')
    return passwd


# check_passwd('hijklmmn', True)
# check_passwd('abbceffg', True)
# check_passwd('abbcegjk', True)
# check_passwd('abcgghh', True)
# check_passwd('aaaaaaa', True)
# check_passwd('abcdffaa', True)
# check_passwd('ghjaabcc', True)
# 
# print(inc_pw('aa'))
# print(inc_pw('az'))
# print(inc_pw('aiolqqqq'))
# print(inc_pw('zz'))

_ = next_passwd('abcdefgh')
_ = next_passwd('ghijklmn')
new_pw = next_passwd('cqjxjnds')
_ = next_passwd(new_pw)