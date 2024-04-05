import pytest
"""
    pytest 标志传参
"""
@pytest.fixture()
def init_data(request):
    print("前后处理")
    # 指定 获取 名称 的 参数
    # 这里的request 是 pytest 自定义 的 无法修改

    maker = request.node.get_closest_marker("data_type")
    print("print",maker)

# 通过mark标记传参的名称 参数 可以是多个
@pytest.mark.data_type(34)
def test_data(init_data):
    print("param")
# 数据驱动 fixture 会迭代这些数据
data = {1,2,3}
# ids 是  唯一 表示 params 可以是数组、元组、列表、字典 可以实现 多级迭代
@pytest.fixture(params=data,ids=[1,2,3])
def init_data(request):
    print("init_data参数是:",request.param)
    return request.param

def test_data1(init_data):
    print("datainit ;",init_data)

if __name__ == '__main__':
    pytest.main(["-v",'-s'])
