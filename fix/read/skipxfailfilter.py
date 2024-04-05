import sys
import warnings

import pytest


# skip 支持代码和注解
@pytest.mark.skip("测试跳过测试方法")
def test_skip():
    print("skip")
    pytest.mark.skip("代码")


# 只支持注解
@pytest.mark.skipif(sys.version_info >= (3, 5), reason="python 的 版本已经不适配")
def test_skipif():
    print("skipif")


# xfail 标记该测试用例会失败
@pytest.mark.xfail()
def test_1_xfail():
    print("xfail")
    raise Exception("自定义异常")


# 明确预期 会 抛出 异常 导致 失败
@pytest.mark.xfail(raises=RuntimeError)
def test_2_xfail():
    print("xfail exception")


# 提示失败原因
@pytest.mark.xfail(reason="xfail失败测试")
def test_3_xfail():
    print("xfail reason")


# 严格模式 就是 与 预期结果 不一致 还是 不通过 fail ，通过 xpass 也 不管
@pytest.mark.xfail(strict=False)
def test_4_xfail():
    print("xfail yange")


#  不会执行
@pytest.mark.xfail(run=False)
def test_5_xfail():
    print("xfail fail")


# 代码标志xfail
def test_6_xfail():
    if 1 == 1:
        pytest.xfail(reason="代码xfail")


@pytest.mark.xfail(sys.version_info > (3, 6), reason="条件xfail")
def test_7_xfail():
    pass


# 警告
def api():
    '''
    warning 这是基类
    userWarning 默认警告
    :return:
    '''
    warnings.warn(UserWarning("版本不适配"))


# 过滤警告 filterwarning
@pytest.mark.filterwarnings("ignore:.*v2")
@pytest.mark.filterwarnings("ignore::UserWarning")
@pytest.mark.filterwarnings("ignore:::test_1_filterwarnings")
def test_v2():
    api()


if __name__ == '__main__':
    # 配置过滤警告
    pytest.main(['-vs', '-W error::UserWarning', __file__])
