import re

#1 this function matches both styles of writing, by checking if the letter is there

"""
text = "color colour"
pattern = "colou?r"

print(re.findall(pattern,text))

"""


#2 searches for emails with top level domain gmail.com or deliveryhero.com

#it searches for a non-word from 0 to 25 characters at beginning, than @, than for a TLD either gmail or deliveryhero, than .com


"""


text = "alex@gmail.com or hero@deliveryhero.com"

pattern = r"(\W|^)[\w.\-]{0,25}@(gmail|deliveryhero)\.com(\W|$)"

print(re.findall(pattern,text))
"""


#3 it seems like it looks for passwords

#it searches for any lowcase character, followed by uppercase , followed by any digit, all in all length 6-12 characters
"""
pattern = r"^(?=.\*[a-z])(?=.\*[A-Z])(?=.\*\d).{6,12}$"


text 
"""
#4 searches for a certain color


#5 searches for a text that ends with done$

