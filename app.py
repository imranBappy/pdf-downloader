import os
import webbrowser as wb
import sys
import requests
url = "http://subeen.com/download/process.php"


info = {"name": "fake", "email": "fake@gmail.com", "country": "BD"}
res = requests.post(url, data=info)

if res.ok is False:
    sys.exit("Error!")

with open("book.pdf", "wb") as f:
    f.write(res.content)

wb.open(os.path.realpath("book.pdf"))
print("Download complate!")
