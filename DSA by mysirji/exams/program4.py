#To convert infix expression 3+4*(5-6/7) into prefix expression
def is_operator(char):
    return char in {'+','-','*','/'}

def get_precedence(operator):
    precedence = {'+': 1, '-': 1, '*':2, '/': 2}
    return precedence.get(operator, 0)

def infix_to_prefix(infix_expression):
    operators = []
    operands = []
    result = []

    for char in infix_expression[::-1]:
        if char.isalnum():
            operands.append(char)
        elif char == ')':
            operators.append(char)
        elif char == '(':
            while operators and operators[-1] != ')':
                operands.append(operators.pop())
            operators.pop()
        elif is_operator(char):
            while operators and get_precedence(operators[-1]) > get_precedence(char):
                operands.append(operators.pop())
            operators.append(char)

    while operators:
        operands.append(operators.pop())

    result = ''.join(operands[::-1])
    return result

#Example usage:
infinix_expression = "3+4*(5-6/7)"
prefix_expression = infix_to_prefix(infinix_expression)
print("Infinix Expression:", infinix_expression)
print("Prefix Expression:", prefix_expression)



