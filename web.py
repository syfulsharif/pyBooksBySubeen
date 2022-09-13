import requests
url = "http://sharif.live"
response = requests.get(url)
with open("sharif.html", "w") as website:
    website.write(response.text)
