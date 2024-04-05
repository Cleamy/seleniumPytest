import allure
import pytest

# ficture 的 作用 范围
'''
function 
class
module
package
session

执行顺序：session>package>module>class>function

每一类的ficture可以时多个，同类按书写的顺序



'''


#
@allure.epic('测试用例allure一级标题')
@allure.feature('测试用例allure二级标题')
@allure.story("用例名")
@allure.title("用例的标题")
@allure.description("用例的描述")
@pytest.fixture(scope="function")
def module_data():
    print("module")

@allure.epic('测试用例allure一级标题')
class TestRange:
    # 动态名称

    @pytest.fixture(params=(1,2,3,4))
    def init_data(self,a,b,d,e):
        # 以代码的形式进行动态格式
        allure.dynamic.feature(f'测试用例allure二级标题{a}参数')
        allure.dynamic.story(f"用例{b}参数")
        allure.dynamic.title(f"用例的{d}标题")
        allure.dynamic.description(f"用例的{e}描述")

        print("init_method")

    def test_file(self,init_data):
        print("test")