import pytest


def test_valid_string(stringinput):
    print("para",stringinput)

if __name__ == '__main__':
    pytest.main(["-vs","--stringinput=hello","--stringinput=world",__file__])
