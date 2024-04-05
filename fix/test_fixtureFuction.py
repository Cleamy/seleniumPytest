import pytest

# fixture 入门实例
"""
    fixture 可以 通过 yield 来区分 前后置
"""

class TestPi:
    # 对 所有 方法其 作用
    @pytest.fixture(autouse=True)
    def init_data(self):
        print("我是前置init_data")
        yield 10
        print("test aftre")

    @pytest.fixture()
    def init_data1(self):
        print("yeild")
        return 10

    #将会调用 init_data 方法
    #通过 pytest.mark.userfixtures()来调用  或者 通过形参中包含 function名词
    @pytest.mark.usefixtures('init_data','init_data1')
    def test_data(self,init_data,init_data1):
        assert init_data == 10
        print("test_data")
        print(init_data1)

if __name__ == '__main__':
    pytest.main()
