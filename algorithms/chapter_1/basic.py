# coding: utf-8
"""
How to read stdin in python?
For example,
name = raw_input("Enter your name: ")   # Python 2.x
or
name = input("Enter your name: ")   # Python 3
"""


def three_value_equal():
    numbers = raw_input('Input three numbers splited by ",":')
    number_list = numbers.split(',')
    if len(number_list) != 3:
        print "Something wrong."
        return
    try:
        number_list = [int(x) for x in number_list]
    except Exception, e:
        print "Int only."
        return
    if len(set(number_list)) == 1:
        print 'equal'
    else:
        print 'not equal'


def int2bin(i):
    if i == 0:
        return "0"
    s = ''
    while i:
        if i & 1 == 1:
            s = "1" + s
        else:
            s = "0" + s
        i /= 2
    return s


if __name__ == '__main__':
    # three_value_equal()
    print int2bin(10)
