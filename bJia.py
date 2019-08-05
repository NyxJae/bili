import re
import os
import requests
import bXiaZai

# xnr文件的地址 pn={}页数 id= 收藏夹编号，在浏览器收藏夹地址栏可找到
url = 'https://api.bilibili.com/medialist/gateway/base/spaceDetail?media_id=295011829&' \
      'pn={}&ps=20&keyword=&order=mtime&type=0&tid=0&jsonp=jsonp'
page = 1


def getHTMLText(url, code='utf-8'):
    kv = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:54.0) Gecko/20100101 Firefox/54.0',
          'Referer': 'https://account.chsi.com.cn/passport/login?service=https://my.chsi.com.cn/archive/j_spring_cas_security_check', }
    try:
        r = requests.get(url, timeout=30, headers=kv)
        # 需手动抛异常 404之类的
        r.raise_for_status()
        r.encoding = code
        return r.text
    except Exception as e:
        print('收藏夹获取失败', e)
    return


for i in range(page):
    shouCangUrl = url.format(i + 1)
    # 得到txt准备分析
    html = getHTMLText(shouCangUrl)
    # 正则找视频av号
    videoHtmls = re.findall('"link":"bilibili:/.{13,18}",', html)
    # 每页有20个视频，分别处理和获取
    for j in range(20):
        # 提取av号
        videoHtml = re.search('o/[0-9]*', videoHtmls[j])
        videoHtml = re.sub('o/', '', videoHtml.group())
        bXiaZai.bXiaZai(bXiaZai.av2url(videoHtml), 'D:\下载\飞鸟')
