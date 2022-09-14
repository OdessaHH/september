"""
#1
text = "Berlin is a world city of culture, politics, media and science."

print("The first white-space character is located at position:" ,text.find(" "))

"""

#2
"""
text = "Berlin is surrounded by the State of Brandenburg and contiguous with Potsdam, Brandenburg's capital."

if text.find("Frankfurt") == -1:
    print("None")
"""


#3

import re
text = "Berlin is a city of culture."

#print(text.replace(" ","-"))

print(re.sub("\s","-",text))

"""
#4

import re 

text = "Berlin is a city of culture."

text_pattern = "(in)"

print(re.search(text_pattern,text))


"""


"""
#5

import re 

text = "Berlin is a city of culture."

text_pattern = "[B]+[a-z]*"

print(re.match(text_pattern, text))

"""

#6

"""

import re 

text = "The rain in Spain."
text_pattern = "ai"
print(len(re.findall(text_pattern,text)))

"""