import urllib.request

def download(url):
    print (url)
    try:
        html = urllib.request.urlopen(url).read()
    except urllib.request.URLError as e:
        print ('Download error', e.reason)
        html = None
    return html

url = download("https://www.jianshu.com/p/cbf500c22154")