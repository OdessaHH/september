import re


text_to_be_searched = """Hey Mr. Bezos,

I hope its okay I message you in this unsecure email program. Sry about that!
Here the list of extremely confidential clients and close coworkers of you who actually visited Epsteins island. Oh boy how I hope no random Python Students extract this sensitive list with some kind of regular expressions! 

therealjeffbezos@bossnet.com
markzuckerbergtheman@facebookormetaidkmail.com
donaldtothatrump@getthatcapitolmail.com
2pacaintdeadandnowchillinonwrongislands@mail.com

Kind regards,
Tanisha"""



email_pattern = "[a-zA-Z0-9]+@[a-zA-Z]+.com"
name_pattern = "(epstein)|(Epstein)"

#x = re.search(pattern, text_to_be_searched)  # using the pattern to search the target text
x = re.findall(email_pattern, text_to_be_searched)
y = re.findall(name_pattern,text_to_be_searched)

print(x)  # printing out the match
print(y)