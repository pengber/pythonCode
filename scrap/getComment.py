import requests
import json
def single_page_comment(link):
    headers = {
    'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:67.0) Gecko/20100101 Firefox/67.0',
    'host-name': 'api-zero.livere.com'
    }
    r = requests.get(link, headers = headers)
    print("---------------------------------------")
    json_string = r.text
    json_string = json_string[json_string.find('{'):-2]
    json_data = json.loads(json_string)
    comment_list = json_data['results']['parents']
    for eachone in comment_list:
        comment = eachone['content']
        print(comment)

for page in range(1,5):
    link1 = "https://api-zero.livere.com/v1/comments/list?callback=jQuery112403473268296510956_1531502963311&limit=10&offset="
    link2 = "&repSeq=4272904&requestPath=%2Fv1%2Fcomments%2Flist&consumerSeq=1020&livereSeq=28583&smartloginSeq=5154&_=1531502963316"
    page_str = str(page)
    link = link1 + page_str + link2
    print(link)
    single_page_comment(link)