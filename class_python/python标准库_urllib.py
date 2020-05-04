### 进行网络请求

import urllib.request


###一般爬虫、抓包等就是拿的一个页面的返回值
response = urllib.request.urlopen('http://www.baidu.com')  # 获取网络请求
print(response.status)
print(response.read())  # 去url里面请求的一个response(返回值）
print(response)
print(response.headers)

"""
现在建议使用Requster package 来获取接口请求
"""

import requests


