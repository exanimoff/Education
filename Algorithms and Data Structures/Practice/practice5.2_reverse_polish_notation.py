def evaluate(expression):
    stack = []

    for token in expression:
        print(stack)
        if token.isdigit():
            stack.append(float(token))
        else:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                result = operand1 + operand2
            elif token == '-':
                result = operand1 - operand2
            elif token == '*':
                result = operand1 * operand2
            elif token == '/':
                result = operand1 / operand2
            stack.append(result)

    return stack[0]

expression = ["2", "1", "+", "3", "*"]
result = evaluate(expression)
print(result)
