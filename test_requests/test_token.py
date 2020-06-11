import requests

class TestToken:
    def test_token(self):
        corpid = "ww441338b28c377647"
        corpsecret = "7-Dbm-lumcWei3dpn-1tof-JmxC1sApIIKAnhkhYVi0"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid={corpid}&corpsecret={corpsecret}"
        r = requests.get(url=url)
        print(r.json())

    def test_token2(self):
        corpid = "ww441338b28c377647"
        corpsecret = "7-Dbm-lumcWei3dpn-1tof-JmxC1sApIIKAnhkhYVi0"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid":"ww441338b28c377647",
            "corpsecret" : "7-Dbm-lumcWei3dpn-1tof-JmxC1sApIIKAnhkhYVi0"
        }
        r = requests.get(url=url, params=params)
        print(r.json())
