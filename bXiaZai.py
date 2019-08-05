import re
import os
import requests


# 获取网页
def getHTMLText(url, code='utf-8'):
    kv = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.11 (KHTML, like Gecko) Chrome/17.0.963.56 Safari/535.11",
        'Referer': 'https://account.chsi.com.cn/passport/login?service=https://my.chsi.com.cn/archive/j_spring_cas_security_check', }
    try:
        r = requests.get(url, timeout=30, headers=kv)
        # 需手动抛异常 404之类的
        r.raise_for_status()
        r.encoding = code
        return r.text
    except Exception as e:
        print('视频页面获取失败', e)
        return
    return


# 将av号转成URL，按需使用
def av2url(av):
    av = str(av)
    url = 'https://www.bilibili.com/video/av{}'.format(av)
    return url


# 实际下载方法(视频地址，本地储存地址，下第几p（缺省则全下）)
def bXiaZai(videoUrl, localUrl, p=0):
    # 获取分p数
    if p is 0:
        try:
            print('全下')
            text = getHTMLText(videoUrl)
            videoNums = re.findall('"videos":[0-9]*', text)
            videoNum = re.sub('"videos":', '', videoNums[0])
            # 不知为啥有的视频get不到，get不到得跳过呀，不能卡在这
            if text is None:
                return
        except:
            print('没有')
    else:
        # 单下某p
        print('单下')
        url = videoUrl + '?p={}'.format(p)
        print(url)
        dow = r'cd /d ' + localUrl + ' && you-get ' + url
        print(dow)
        os.system(dow)
        return
    # 下载每p
    for j in range(int(videoNum)):
        url = videoUrl + '?p={num}'.format(num=j + 1)
        # 用you-get调用控制台下载
        dow = r'cd /d ' + localUrl + ' && you-get ' + url
        print(dow)
        os.system(dow)
     return


if __name__ == '__main__':
    bXiaZai(av2url(17496645), r'D:\下载\飞鸟' )
