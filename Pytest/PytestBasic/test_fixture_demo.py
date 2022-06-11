import pytest

@pytest.yield_fixture()
def browser_config():
        print("Chrome Launch Success")

        yield
        print("Browser Close")

def test_valid_login(browser_config):
        print('Valid Login Success')

def test_invalid_login(browser_config):
        print('Invalid Login Success')