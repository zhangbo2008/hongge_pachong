# https://favird.com/l/ai-tools-and-applications




# !pip install lxml  # 安装lxml库
from lxml import etree
parser = etree.HTMLParser(encoding="utf-8")
parser=parser

tree = etree.parse("aa.html",parser=parser)  # 此案例已经上传到目录
print(1)


list1 = tree.xpath('//div[@class="product-text relative"]/div[@class="product-text-title text-gray"]/text()')
list2 = tree.xpath('//div[@class="product-text relative"]/div[@class="product-text-desc text-gray"]/text()')
list3 = tree.xpath('//div[@class="product-text relative"]/span[@class="item-categories text-gray-2"]/text()')
a=(zip(list1,list2,list3))
a=list(a)
import json
aaaa=open('aaaa.json','w') 
b=json.dump(a,aaaa)
