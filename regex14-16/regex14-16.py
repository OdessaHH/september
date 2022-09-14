import re

#14
"""
text = input("enter your stuff: ")
lrem = re.sub("^0+0$","",text)
print(re.sub("0+$","",lrem))

"""
#15

"""
pattern = r"\d\s*(\+|-|\*|\/|%)\s*\d"

intx = input("enter your shit:")


if (re.search(pattern, intx)) == None:
    print(False)
else:
    print(True)

"""

#16

#pat1 = r"(:|8|;|x)\("

inp = input("enter smileys: ")

#pat2 = r":)|8)|;|x)"

#print(re.sub(pat1,pat2,inp))



eyes = [r":",r";", r"8", r"x"]
for e in eyes:
    pat1 = e +r"\("
    pat2 = e +r")"
    finds = re.sub(pat1,pat2,inp)
print(finds)