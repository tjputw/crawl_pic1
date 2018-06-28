#http://sc.chinaz.com/tupian/shanshuifengjing_2.html

#'http://pic.sc.chinaz.com/Files/pic/pic9/201806/bpic7141_s.jpg'   虚拟地址
# real_url = 'http://fjdx.sc.chinaz.com/Files/DownLoad/    pic9/201806/bpic7081.rar'
from lxml import etree
import requests, urllib
import urllib.request
import re

url = 'http://sc.chinaz.com/tupian/shanshuifengjing.html'
url_multi = 'http://sc.chinaz.com/tupian/shanshuifengjing_%d.html'
real_url = 'http://fjdx.sc.chinaz.com/Files/DownLoad/%s.rar'
#real_url = 'http://fjdx.sc.chinaz.com/Files/DownLoad/pic9/201704/zzpic2643.rar'
# real_url1 = 'http://fjdx.sc.chinaz.com/Files/DownLoad/pic9/201806/bpic7081.rar'
# img_list =       'http://pic.sc.chinaz.com/Files/pic/pic9/201806/bpic7081_s.jpg'

page = int(input('请输入需要下载的页数：'))

for i in range(page):
    if i == 0:
        response = requests.get(url=url)
    else:
        response = requests.get(url=url_multi % (i+1))
    response.encoding = 'utf-8'
    content = response.text

    with open('./pic%d.html' %(i+1),'w',encoding='utf-8') as fp:
        fp.write(content)

    res = etree.HTML(content)

    img_list = res.xpath('//div[@class="box picblock col3"]/div/a/img/@src2')
    name_list = res.xpath('//div[@class="box picblock col3"]/div/a/img/@alt')
    # print(img_list)
    # print(name_list)

    for i in range(len(img_list)):
        suffix = img_list[i][35:-6]
        print(real_url % suffix)
        urllib.request.urlretrieve(url=real_url % suffix,filename='../download/pic/%s.rar'% name_list[i])
        print('----下载成功--------')

