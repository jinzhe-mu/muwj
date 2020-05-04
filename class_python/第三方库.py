import pytest
import requests

# 当返回时200的时候，说明访问成功
# r = requests.get("http://www.baidu.com")
# print(r.status_code)
# print(r.encoding)  # 返回一个编码
# print(r.text)
# r.encoding = "utf-8"  # 出现乱码的时候先转码(设置编码格式)
# print(r.text)
r = requests.post('http://httpbin.org/post', data={'key':'value'})
# print(r1.status_code)
print(r.text)