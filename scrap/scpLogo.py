from urllib.request import urlretrieve
from urllib.request import urlopen
import requests
from bs4 import BeautifulSoup

headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 6pip.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.82 Safari/537.36',
        'Host': 'beijing.anjuke.com'
    }
link = 'http://www.pythonscraping.com'
r = requests.get(link, headers= headers)

print(r.text)

print("----------------------")
html = urlopen('http://www.pythonscraping.com')
bsobj = BeautifulSoup(html)
imgLocation = bsobj.find("a", {"id":"logo"}).find("img")['src']

print(html)


urlretrieve(imgLocation, "logo.jpg")
