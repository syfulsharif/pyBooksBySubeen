import re

s = "Bangladesh is our homeland"
match = re.search("B\w+h", s)

print(match.group())
