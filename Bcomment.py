import json
import requests
import pprint
headers ={
    'referer': 'https://www.bilibili.com/video/BV1t3411p7Vq?spm_id_from=444.41.0.0',
    'user-agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.69 Safari/537.36 Edg/95.0.1020.53',
}
main_url = 'https://api.bilibili.com/x/v2/reply/main?'
main_params = {
    'jsonp': 'jsonp',
    'next': 0,
    'type': '1',
    'oid': '425009881',
    'mode': '2',
    'plat': '1',
    '_': '1648289436898'
}
reply_url = 'https://api.bilibili.com/x/v2/reply/reply'
reply_params = {
    'jsonp': 'jsonp',
    'pn': '1',
    'type': '1',
    'oid': '425009881',
    'ps': '10',
    'root': '106841868432',
    '_': '1648290346968'
}
dic = {}
def parse_reply(root):
    requests.get(url=reply_url, headers=headers, params=reply_params).json()
def parse_main_reply():
    page_text = requests.get(url = main_url, headers = headers,params = main_params).json()
    with open('test.html','w',encoding='utf-8') as fp:
        fp.write(page_text)
    for comment in page_text['data']['replies']:
        dic['username'] = comment['member']['uname']
        dic['content'] = comment['content']['message']
        dic['reply_count'] = comment['rcount']
        dic['reply_id'] = comment['rpid']
        dic['like_count'] = comment['like']
        dic['total_reply_num'] = page_text['data']['cursor']['all_count']
        dic['is_end'] = page_text['data']['cursor']['is_end']
        print(dic)
        f.write(str(dic['username'])+dic['content']+str(dic['reply_count'])+str(dic['reply_id'])+str(dic['like_count'])+str(dic['total_reply_num'])+str(dic['is_end'])+'\n')
    if dic['is_end'] == False:
        main_params['next'] += 1
        return parse_main_reply()
f = open('test','a',encoding='utf-8')
parse_main_reply()
f.close()