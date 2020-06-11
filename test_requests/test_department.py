import requests

class TestDepartment:
    def setup(self):
        corpid = "ww441338b28c377647"
        corpsecret = "7-Dbm-lumcWei3dpn-1tof-JmxC1sApIIKAnhkhYVi0"
        url = f"https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid":"ww441338b28c377647",
            "corpsecret" : "7-Dbm-lumcWei3dpn-1tof-JmxC1sApIIKAnhkhYVi0"
        }
        r = requests.get(url=url, params=params)
        self.token = r.json()['access_token']

    def test_create_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/department/create"
        params = {
            "access_token": self.token
        }
        json = {
            "name": "系统管理部2",
            "name_en": "XTGLB2",
            "parentid": 1,
            "order": 1,
            "id": 22
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"]==0


    def test_update_department(self):
        pass

    def test_delete_department(self):
        pass

    def  test_getlist_department(self):
        pass