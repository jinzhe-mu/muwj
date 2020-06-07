"""
This example shows how to send a reply from the proxy immediately
without sending any data to the remote server.
"""
from mitmproxy import http


# request不能被改变，是写死的
def request(flow: http.HTTPFlow) -> None:
    # pretty_url takes the "Host" header of the request into account, which
    # is useful in transparent mode where we usually only have the IP otherwise.
    # 如果url中有 quote.json
    if "v5/stock/batch/quote.json" in flow.request.pretty_url:
        # 打开本地的json文件
        with open("C:/Users/Administrator/Desktop/xueqiu2.json", encoding="utf-8") as f:
             # 将json文件内容放入返回结果
             #加入路径后需要把路径下的分隔符"\"修改为"/"，因为"\"为转义字符
            flow.response = http.HTTPResponse.make(
                200,  # (optional) status code
                f.read(),  # (optional) content
                {"Content-Type": "application/json"}  # (optional) headers
            )