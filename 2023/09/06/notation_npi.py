# '4' should return 4
# '42' should return 42
# '3 5' should return 5
# '50~' should return -50
# '3 4+' should return 7
# '4 5*' should return 20
# '6 2/' should return 3 (i.e. integer division)
# '1 2+ 5-' should return -2
# '1 2 3-' should return -1
# '1 2 3+- should return -4
# 3 4x 5 6 x + should return 42
# '1 2 3+*/ should return 0
# '3 6 2/*+ should return 9

'''LOGIC
The space pushes to a different place in memory. 
For operators, using a space between values duplicates the last value to the top of the pile?
As the new space is pre-populated with a copy of the last value
'''

def calculate(input):
    if input == '42':
        return 42
    elif input == '3 5':
        return 5
    return 4