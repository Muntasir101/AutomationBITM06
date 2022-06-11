import pytest

@pytest.mark.run(order=4)
def test_method5():
    print('Hello world')

@pytest.mark.run(order=3)
def test_method6():
    print('Hello Dhaka')

@pytest.mark.run(order=2)
def test_method7():
    print('Hello BITM')

@pytest.mark.run(order=1)
def test_method8():
    print('Hello PnT')
