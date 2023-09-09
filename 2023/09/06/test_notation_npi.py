from notation_npi import calculate
# 3 4x 5 6x+ should return 42
# '-' should return 0
# '-50' should return 50

'''LOGIC
The space pushes to a different place in memory. 
For operators, using a space between values duplicates the last value to the top of the pile?
As the new space is pre-populated with a copy of the last value
'''

def test_digit_string_returns_the_digit():
    assert calculate('4') == 4

def test_single_operand_string_returns_operand():
    assert calculate('42') == 42

def test_two_operands_with_space_returns_last_one():
    assert calculate('3 5') == 5

def test_unique_operator():
    assert calculate('50-') == -50
    assert calculate('3+') == 3

def test_addition_two_operands():
    assert calculate('3 4+') == 7

def test_multiplication_two_operands():
    assert calculate('4 5*') == 20

def test_division_two_operands():
    assert calculate('6 2/') == 3
    assert calculate('2 6/') == 0

def test_operation_three_operands():
    assert calculate('1 2 3-') == -1
    assert calculate('1 2- 3+') == 2
    assert calculate('1 2+ 3-') == 0
    assert calculate('10 20+ 50-') == -20

def test_stacked_operators():
    assert calculate('1 2 3+-') == -4
    assert calculate('1 2 3-+') == 0
    assert calculate('1 2 3+/') == 0

def test_too_many_operators():
    assert calculate('1 2 3+*/') == 0
    assert calculate('3 6 2/*+') == 9
    assert calculate('3 6 2/+*') == 0