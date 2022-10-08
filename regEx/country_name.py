import re


import re

s = "Afganistan, America, Bangladesh, Canada, Denmark, England, Greenland, Iceland, Netherlands, New Zealand, Sweden, Switzerland"

countrues = s.split(",")
# print(countrues)

## This is the code without using regEx
# country_endswith_land = [
#     item for item in countrues if item.endswith("land") or item.endswith("lands")
# ]
# print(country_endswith_land)

# The following code used RegEX
li = re.findall(r"(\w+lands*)", s)

print(li)
