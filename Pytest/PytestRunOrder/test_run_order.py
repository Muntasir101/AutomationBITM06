import pytest

@pytest.mark.run(order=4)
def test_method1():
    print('Hello world')

@pytest.mark.run(order=3)
def test_method2():
    print('Hello Dhaka')

@pytest.mark.run(order=2)
def test_method3():
    print('Hello BITM')

@pytest.mark.run(order=1)
def test_method4():
    print('Hello PnT')
