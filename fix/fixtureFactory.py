import pytest
# 在一个业务中多次调用多个fixture

@pytest.fixture()
def register():
    def _register(user):
        print("注册函数:",user)
        result=True
        return result

def test_case_1(register):
        register = register("login")
        print(register)


if __name__ == '__main__':
    pytest.main()