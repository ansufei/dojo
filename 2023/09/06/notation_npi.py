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
    queue = []
    length_input = len(input)
    counter = 0
    while counter < length_input:
        if input[0] == ' ':
            queue.append(input[0])
        else:
            if queue:
                queue[-1] += input[0]
            else:
                queue.append(input[0])
        input = input[1:]
        counter += 1
    return int(queue[-1])

calculate('3 5')