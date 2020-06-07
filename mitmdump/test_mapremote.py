import json

def response(flow):
    # 判断url是否存在"v5/stock/batch/quote.json"（有多个quote.json需要根据路径明确到具体的
    if "v5/stock/batch/quote.json" in flow.request.pretty_url:
        # 返回结果json化
        res = json.loads(flow.response.content)
        # 对返回结果进行篡改
        res["data"]["items"][1]["quote"]["name"] = "jinzhe-mu2020!!!!!"
        res["data"]["items"][1]["quote"]["current"] = "0.8888888"
        # 返回结果的二次赋值
        flow.response.text = json.dumps(res)