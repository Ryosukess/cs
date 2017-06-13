# !/usr/bin/python
# encoding: UTF-8

import re


pattern_number = re.compile(r'\d+')
pattern_letter = re.compile(r'\D+')
str1 = '1a2b3c4d5f6g'

print pattern_number.findall(str1)
print pattern_letter.findall(str1)
print pattern_number.split(str1)
print pattern_letter.split(str1)
print pattern_number.search(str1)
print pattern_number.match(str1)
print pattern_number.sub(str1)
print pattern_number.subn(str1,'b')


'''
output:
 ['2', '32324', '3', '4', '3', '4', '3', '324', '3', '4', '32']
['dkajkkj', 'k', 'k', 'j', 'k', 'j', 'k', 'jn', 'j', 'bn', 'b']
'''



'''
替换字符串中的空格

a="1721 skdjksj  1313"
print a
a=a.replace(' ','')
print a
''' 
