import pytest

#使用conftest中的数据
# @pytest.fixture(scope="module")
# def connectDB():
#     print("连接数据库操作")
#     yield
#     print("断开数据库连接")

class TestDemo:

    def test_a(self,connectDB):
        print("测试用例a")

    def test_b(self,connectDB):
        print("测试用例b")

class TestDemo2:

    def test_a(self,connectDB):
        print("测试用例a")

    def test_b(self,connectDB):
        print("测试用例b")