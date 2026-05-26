"""Testing the mathematical operation that are done in the app"""
from app import add,subtract,multiply,divide

def test_add():
    """Testing the add function"""
    assert add(5,10)==15 

def test_subtract():
    """testing the subtract function"""
    assert subtract(10,5)==5

def test_multiply():
    """Testing the multiply function"""
    assert multiply(10,5)==50

def test_divide():
    """Testing the divide function"""
    assert divide(50,5)==10
    