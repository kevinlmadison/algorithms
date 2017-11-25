#!/usr/bin/env python3

''' These functions are from the book Elements of Programming Interviews in Python 
    and are simply for learning purposes and practice. Unless explicitly stated I
    do not take credit for writing these functions.
'''

# This function tests if a string is a palindrome.
def is_palindrom(s):
    # ~i is the same as -i - 1 
    return all(s[i] == s[~i] for i in range(len(s)))

# This function converts a string to an int.
def str_to_int(s):
    # This function is actually an excellent example of the utility of
    # lambda functions in combination with the reduce function. Here the
    # third parameter of reduce is a 0 which is the optional initializer.
    # This is what sets rsum to the initial value of 0 instead of setting
    # it to the first value of the iterator.
    return reduce((lambda rsum, c: rsum * 10 + string.digits.index(c)),
                    s[s[0] == '-':], 0) * (-1 if s[0] == '-' else 1)

# This function converts an int to a string.
def int_to_str(i):
    # We need to save the sign of the number so that we can operate
    # on its absolute value.
    is_negative = False
    if i < 0:
        i, is_negative = -i, True

    # We isolate the last digit and add it to the ascii value of zero
    # and then convert this new value back into a character.
    # We then remove the least significant digit by way of integer division.
    s = []
    while i:
        s.append(chr(ord('0') + i % 10))
        i //= 10 

    # We need to reverse the order of s before printing because we wanted to
    # save time by not appending to the front when s was created. We also 
    # re-apply the sign if needed.
    return ('-' if is_negative else '') + ''.join(reversed(s)) 

# This function takes a numeric string with base b1 and converts it to base b2
def convert_base(num_as_string, b1, b2):
    def construct_from_base(num_as_int, base):
        return ('' if num_as_int == 0 else
                construct_from_base(num_as_int // base, base)
                + string.hexdigits[num_as_int % base].upper())

    is_negative = num_as_string[0] == '-'
    num_as_int = reduce(lambda x, c: x * b1 + string.hexdigits.index(c.lower()),
            num_as_string[is_negative:], 0)

    return ('-' if is_negative else '') + ('0' if num_as_int == 0 else
                                            construct_from_base(num_as_int, b2))

# This is the main function for testing these nice functions.
if __name__ == '__main__':
    # Here we test the function is_palindrome.
    s1, s2 = 'racecar', 'holiday'
    print(str(is_palindrom(s1)))  # This should print True.
    print(str(is_palindrom(s2)))  # This should print False.

    # Here we test the funtion int_to_str.
    i1, i2 = 3049, 1337
    print(int_to_str(i1))  # This should print 3049.
    print(int_to_str(i2))  # This should print 1337.

    # Here we test the function str_to_int.
    s1, s2 = '1337', '1234567'
    print(str(s1))  # This prints 1337
    print(str(s2))  # This prints 1234567
