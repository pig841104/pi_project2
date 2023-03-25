import urllib.request as req
url="https://www.cwb.gov.tw/V8/C/W/index.html"
with req.urlopen(url) as response:
    data=response.read().decode("UTF-8")
import bs4
root=bs4.BeautifulSoup(data, "html.parser")
print(root.title)