import requests
import os
import webbrowser as wb

url = "http://sharif.live"

response = requests.get(url)
with open("sharif2.html", "w", encoding=response.encoding) as f:
    f.write(response.text)

file_path = os.path.realpath("sharif2.html")
print(file_path)

wb.open("file://" + file_path)
