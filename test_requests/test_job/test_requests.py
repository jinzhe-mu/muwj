import requests

class TestDepartment:
    def setup(self):
        corpid = "ww441338b28c377647"
        corpsecret = "7-Dbm-lumcWei3dpn-1tof-JmxC1sApIIKAnhkhYVi0"
        url = "https://qyapi.weixin.qq.com/cgi-bin/gettoken"
        params = {
            "corpid":"ww441338b28c377647",
            "corpsecret" : "7-Dbm-lumcWei3dpn-1tof-JmxC1sApIIKAnhkhYVi0"
        }
        r = requests.get(url=url, params=params)
        self.token = r.json()['access_token']

    # def teardown(self):
    #     #  关闭应用回收资源
    #     self.driver.quit()



    # 创建标签
    def test_create_label(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/create"
        params = {
            "access_token": self.token
        }
        json = {
            "tagname": "惊蛰4",
            "tagid": 15
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 更新标签名字
    def test_update_label(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/update"
        params = {
            "access_token": self.token
        }
        json = {
            "tagid": 15,
            "tagname": "惊蛰5"
            }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 删除标签
    def test_delete_label(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/delete"
        params = {
            "access_token": self.token,
            "tagid": "15"
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 获取标签成员
    def  test_getlist_department(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/get"
        params = {
            "access_token": self.token,
            "tagid": 14
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 增加标签成员
    def test_add_labelmembers(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/addtagusers"
        params = {
            "access_token": self.token
        }
        json = {
            "tagid": 14,
            "userlist": ["a1","a2"],
             "partylist" : [1]
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"] == 0

    # 删除标签成员
    def test_delete_labelmembers(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/deltagusers"
        params = {
            "access_token": self.token
        }
        json = {
            "tagid": 13,
            "userlist": ["a1", "a2"],
            "partylist": [1]
        }
        r = requests.post(url=url, params=params, json=json)
        print(r.json())
        assert r.json()["errcode"] == 0


    # 获取标签列表
    def test_getlist_labelmembers(self):
        url = "https://qyapi.weixin.qq.com/cgi-bin/tag/list"
        params = {
            "access_token": self.token
        }
        r = requests.get(url=url, params=params)
        print(r.json())
        assert r.json()["errcode"] == 0