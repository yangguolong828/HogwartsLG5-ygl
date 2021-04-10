
import pytest
import yaml


def pytest_collection_modifyitems(session, config, items):
    for item in items:
        # item.name用例的名字
        item.name = item.name.encode('utf-8').decode('unicode-escape')

        # 用例的路径
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')

        if 'login' in item.nodeid:
            item.add_marker(pytest.mark.login)

    items.reverse()

def pytest_addoption(parser):
    mygroup = parser.getgroup("Hogwarts")
    mygroup.addoption("--env",
         default='test',
         dest = 'env',
         help = "set your run env"
    )
@pytest.fixture(scope='session')
def cmdoption(request):
    env = request.config.getoption("--env", default="test")
    if env == 'test':
        print("test 环境")
        datapath = "./data/dev/datas.yml"
    elif env == 'dev':
        datapath = "./data/test/datas.yml"

    with open(datapath) as f:
        datas = yaml.safe_load(f)
    return env, datas

