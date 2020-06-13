import requests

class WeWork():
    def get_token(self):
        corpid = "ww441338b28c377647"
        corpsecret = "7-Dbm-lumcWei3dpn-1tof-JmxC1sApIIKAnhkhYVi0"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid":corpid,
            "corpsecret" : corpsecret
        }
        r = requests.get(url=url, params=params)
        self.token = r.json()['access_token']
        return self.token