def math(expression):
    operators = ['+', '-', '*', '/']
    number1 = ''
    final = 0
    calculator = '+'
    expression += '+'
    for l in expression:
        if l not in operators:
            number1 += l
        elif l in operators:
            if calculator == '+':
                final = final + int(number1)
                number1 = '0'
            elif calculator == '-':
                final = final - int(number1)        
                number1 = '0'
            elif calculator == '/':
                final = final / int(number1)
                number1 = '0'
            elif calculator == '*':
                final = final * int(number1)
                number1 = '0'
            calculator = l    
    return int(final)