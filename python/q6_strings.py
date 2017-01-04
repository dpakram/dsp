# Based on materials copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0


import re

def donuts(count):

    if count < 10:
        return "Number of donuts: %d" %(count)
    elif count >= 10:
        return "Number of donuts: many"

    """
    Given an int count of a number of donuts, return a string of the
    form 'Number of donuts: <count>', where <count> is the number
    passed in. However, if the count is 10 or more, then use the word
    'many' instead of the actual count.
    """
'''
print donuts(4)
'Number of donuts: 4'
print donuts(9)
'Number of donuts: 9'
print donuts(10)
'Number of donuts: many'
print donuts(99)
'Number of donuts: many'
'''    


def both_ends(s):
    new_string = ''

    if len(s) >= 2:
        new_string = s[0] + s[1] + s[-2] + s[-1]
        return new_string
    else:
        return ''

    """
    Given a string s, return a string made of the first 2 and the last
    2 chars of the original string, so 'spring' yields 'spng'.
    However, if the string length is less than 2, return instead the
    empty string.
 
    """
'''
print both_ends('spring')
'spng'
print both_ends('Hello')
'Helo'
print both_ends('a')
''
print both_ends('xyz')
'xyyz'
    
'''


def fix_start(s):
    s_list = list(s)
    new_string = s_list[0]
    for i in range(len(s_list)-1):
        if s_list[0] == s_list[i+1]:
            new_string = new_string + '*'
        elif s_list[0] != s_list[i+1]:
            new_string = new_string + s_list[i+1]
    return new_string


    """
    Given a string s, return a string where all occurences of its
    first char have been changed to '*', except do not change the
    first char itself. e.g. 'babble' yields 'ba**le' Assume that the
    string is length 1 or more.
    """
'''
print fix_start('babble')
'ba**le'
print fix_start('aardvark')
'a*rdv*rk'
print fix_start('google')
'goo*le'
print fix_start('donut')
'donut'
'''
#raise NotImplementedError


def mix_up(a, b):
    new_string = b[0] + b[1] + a[2:] + ' ' + a[0] + a[1] + b[2:]
    print new_string


    """
    Given strings a and b, return a single string with a and b
    separated by a space '<a> <b>', except swap the first 2 chars of
    each string. Assume a and b are length 2 or more.
    """
'''
mix_up('mix', 'pod')
'pox mid'
mix_up('dog', 'dinner')
'dig donner'
mix_up('gnash', 'sport')
'spash gnort'
mix_up('pezzy', 'firm')
'fizzy perm'
'''   
#raise NotImplementedError


def verbing(s):
    if len(s) > 3:
        if "ing" in s:
            new_string = s + "ly"
            return new_string
        elif "ing" not in s:
            new_string = s + "ing"
            return new_string
    else:
        return s


    """
    Given a string, if its length is at least 3, add 'ing' to its end.
    Unless it already ends in 'ing', in which case add 'ly' instead.
    If the string length is less than 3, leave it unchanged. Return
    the resulting string.

    """

'''
print verbing('hail')
'hailing'
print verbing('swiming')
'swimingly'
print verbing('do')
'do'
'''
#raise NotImplementedError


def not_bad(s):

    #Scan through a string, looking for any location where this RE matches.
    #format re.search(pattern, string, flags=0)
    #returns match object match.group()
    return re.sub(r'not\s\w+\sbad', 'good', s)
      
    """
    Given a string, find the first appearance of the substring 'not'
    and 'bad'. If the 'bad' follows the 'not', replace the whole
    'not'...'bad' substring with 'good'. Return the resulting string.
    So 'This dinner is not that bad!' yields: 'This dinner is
    good!'
    """
'''
print not_bad('This movie is not so bad')
'This movie is good'
print not_bad('This dinner is not that bad!')
'This dinner is good!'
print not_bad('This tea is not hot')
'This tea is not hot'
print not_bad("It's bad yet not")
"It's bad yet not"
'''

#raise NotImplementedError


def front_back(a, b):
    
    new_string_a = ''
    new_string_b = ''
    odd_a = (len(a)/2)
    odd_b = (len(b)/2)
    if len(a)%2 == 0:
        new_string_a = a[:len(a)/2]
        if len(b) % 2 == 0:
            new_string_b = b[:len(b)/2] + a[len(a)/2:] + b[len(b)/2:]
        if len(b) % 2 != 0:
            new_string_b = b[:len(b)/2 + 1] + a[len(a)/2:] + b[len(b)-odd_b:]
    if len(a)%2 != 0:
        new_string_a = a[:(len(a)/2)+1]
        if len(b) % 2 == 0:
            new_string_b = b[:len(b)/2] + a[len(a)/2:] + b[len(b)/2:]
        if len(b) % 2 != 0:
            new_string_b = b[:(len(b)/2)+1] + a[len(a)-odd_a:] + b[len(b)-odd_b:]
            
    return new_string_a + new_string_b
    
    

    """
    Consider dividing a string into two halves. If the length is even,
    the front and back halves are the same length. If the length is
    odd, we'll say that the extra char goes in the front half. e.g.
    'abcde', the front half is 'abc', the back half 'de'. Given 2
    strings, a and b, return a string of the form a-front + b-front +
    a-back + b-back
    """
'''
print front_back('abcd', 'xy')
'abxcdy'
print front_back('abcde', 'xyz')
'abcxydez'
print front_back('Kitten', 'Donut')
'KitDontenut'
'''

#raise NotImplementedError
