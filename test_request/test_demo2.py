import requests

class TestContact():

    def test_add_member(self):

        # 获取token
        url_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8d11df16a0576625&corpsecret=go2w1K994D5FO24xp-bMQbTTBwz2YbvJAJexdf0cRYw"
        r_token = requests.get(url_token)
        token = r_token.json()['access_token']

        # 清理数据
        url_delete = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=ceshi12345"
        r_delete = requests.get(url_delete)
        print(r_delete.json())

        # 新建通讯录成员
        url_add = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
        body = {
            "userid": "ceshi12345",
            "name": "测试12345",
            "mobile": "+86 13200000200",
            "department": [1]
        }
        r_add = requests.post(url_add, json=body)

        # 读取成员
        url_get = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=YangGuoLong"
        r_get = requests.get(url_get)
        print(r_get.json())

    def test_delete_member(self):
        # 数据准备
        # 新建通讯录成员
        url_add = f"https://qyapi.weixin.qq.com/cgi-bin/user/create?access_token={token}"
        body = {
            "userid": "ceshi12345",
            "name": "测试12345",
            "mobile": "+86 13200000200",
            "department": [1]
        }
        r_add = requests.post(url_add, json=body)

        # 删除成员
        url_delete = f"https://qyapi.weixin.qq.com/cgi-bin/user/delete?access_token={token}&userid=ceshi12345"
        r_delete = requests.get(url_delete)
        print(r_delete.json())

        # 读取成员
        url_get = f"https://qyapi.weixin.qq.com/cgi-bin/user/get?access_token={token}&userid=YangGuoLong"
        r_get = requests.get(url_get)
        print(r_get.json())