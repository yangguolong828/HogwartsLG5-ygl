
#创建fixture函数
import pytest


@pytest.fixture()
def login():
    print("登录操作")
    print("获取token")
    username = "Tom"
    password = "123456"
    token = "token123456"
    yield[username,password,token]
    print("登出操作")
#测试用例1：需要提前登录
def test_case1(login):
    print(f"login username and password:{login}")
    print("测试用例一")
#测试用例2：不需要提前登录
def test_case2():
    print("测试用例二")
#测试用例3：需要提前登录
def test_case3(login):
    print("测试用例三")
#测试用例4：不需要提前登录
@pytest.mark.usefixtures("login")
def test_case4():
    print("测试用例四")