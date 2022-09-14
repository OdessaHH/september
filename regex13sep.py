# example code:
string_with_newlines = """something
someotherthing"""

import re

print(re.match('some', string_with_newlines)) # matches
print(re.match('someother', 
               string_with_newlines)) # won't match
print(re.match('^someother', string_with_newlines, 
               re.MULTILINE)) # also won't match
print(re.search('someother', 
                string_with_newlines)) # finds something
print(re.search('^someother', string_with_newlines, 
                re.MULTILINE)) # also finds something

m = re.compile('thing$', re.MULTILINE)

print(m.match(string_with_newlines)) # no match
print(m.match(string_with_newlines, pos=4)) # matches
print(m.search(string_with_newlines, 
               re.MULTILINE)) # also matches




"""Python offers two different primitive operations based on regular expressions: 'match' checks for a match only at the beginning of the string, while 'search' checks for a match anywhere in the string """