import os

# 用之前方法下载不能的av号
av = ['1018536', '3047474', '2574255', '7688008', '23114958']
# 对应av号的分p数
num = [4, 1, 1, 13, 3]
for i in range(len(av)):
    for j in range(num[i]):
        try:
            url = 'https://www.bilibili.com/video/av{av}/?p={num}'.format(av=av[i], num=j + 1)
            dow = r'cd /d D:\下载\乃木坂\演唱会 && you-get  ' + url
            os.system(dow)
        except:
            continue
