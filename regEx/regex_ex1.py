import re

s = "Bangladesh"

match = re.search("de", s)
# print(match.group())

sentence = "Bangladesh is our homeland"

# str_search = re.search("B.n...", sentence)
str_search = re.search("............", sentence)
# print(str_search.group())


# String except white space
str_search_without_space = re.search("o\w\w", sentence)
print(str_search_without_space.group())

