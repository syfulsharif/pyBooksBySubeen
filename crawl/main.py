import requests
import re

url = "http://books.toscrape.com/index.html"
response = requests.get(url)
print(response.ok)

text = response.text
print(len(text))
result = re.findall(r'<div class="side_categories">(.*?)</div>', text, re.M | re.DOTALL)
print(len(result))
print(type(result))
print(result)