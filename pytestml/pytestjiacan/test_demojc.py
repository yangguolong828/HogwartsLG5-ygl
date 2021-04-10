import pytest


@pytest.mark.parametrize("name", ["哈利","赫敏"])
def test_demo(name):
    print(name)

def test_login():
    print("login")

def test_login_fail():
    print("login_fail")
    assert False

def test_search():
    print("search")

def test_env(cmdoption):
    # print(cmdoption)
    env, datas = cmdoption
    print(datas)
    host = datas['env']['host']
    port = datas['env']['port']
    url = str(host) + ":" + str(port)
    print(url)