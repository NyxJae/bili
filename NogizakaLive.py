import bXiaZai
import bs4

url = []
# 这是一个乃木坂所有live的索引网址
text = bXiaZai.getHTMLText(
    'http://wiki.akbfun48.com/index.php/%E4%B9%83%E6%9C%A8%E5%9D%82%E6%BC%94%E5%94%B1%E4%BC%9A%E5%90%88%E9%9B%86')
soup = bs4.BeautifulSoup(text, "lxml")
zzr = soup.find_all('a')
for item in zzr:
    if item.get('class') == ['external', 'free']:
        url.append(item.get('href'))

for videoUrl in url:
    bXiaZai.bXiaZai(videoUrl, 'D:\下载\乃木坂\演唱会')
