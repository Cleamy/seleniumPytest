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
@pytest.fixture(scope="function")
def module_data():
    print("module")

class TestRange:

    @pytest.fixture()
    def init_data(self):
        print("init_method")