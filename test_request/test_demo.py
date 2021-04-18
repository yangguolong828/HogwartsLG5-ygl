import requests

class TestLeads():

    def test_request_web(self):

        # # 获取token
        # url_token = "https://qyapi.weixin.qq.com/cgi-bin/gettoken?corpid=ww8d11df16a0576625&corpsecret=go2w1K994D5FO24xp-bMQbTTBwz2YbvJAJexdf0cRYw"
        # r_token = requests.get(url_token)
        # token = r_token.json()['access_token']

        # 读取成员
        url_get = "https://evboe.bytedance.net/ev/growth/baize/lead/query?access_token=ZmYxNjY2MTM1ZHwxNjE0MTUxNjAyOTZ8fDAGBgYGBgY"
        r_get = requests.get(url_get)
        print(r_get.json())
