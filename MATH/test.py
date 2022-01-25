'''
solve for "x" - one step equation
solve for 2x+-5=10  2 step equation
solve for "x", "y", "z" - , multistep equation
'''

# 3x+12=16
x_input = int(input('Number with the X: '))
num_input = int(input('Num without a var: '))
print('ex: +, -')
operation_sign = input('The sign between the var and the real num: ')
answer_input = int(input('Num after the = sign: '))

if operation_sign == '+':
    step_1 = (answer_input - num_input)
    step_2 = (step_1 / x_input)
    print(str(x_input) + 'x ' + operation_sign + ' ' + str(num_input) + ' = X = ' + str(step_2))
elif operation_sign == '-':
    step_1 = (answer_input + num_input)
    step_2 = (step_1 / x_input)
    print(str(x_input) + 'x ' + operation_sign + ' ' + str(num_input) + ' = X = ' + str(step_2))
else:
    print('1')


