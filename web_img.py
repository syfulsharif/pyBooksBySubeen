import requests as req
import os

img_src = "https://assets.thehansindia.com/h-upload/2021/07/31/1092805-tech.webp"
res = req.get(img_src)

with open("tech.webp", "wb") as f:
    f.write(res.content)
