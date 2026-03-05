def priority(ch):
    if ch == '^':
        return 3
    elif ch == '*' or ch == '/':
        return 2
    elif ch == '+' or ch == '-':
        return 1
    return -1


def check_operand(ch):
    return ch.isalnum()  # checks a-z, A-Z, 0-9


def infix_to_postfix(expression):
    stack = []
    result = ""

    for ch in expression:
        if check_operand(ch):
            result += ch

        elif ch == '(':
            stack.append(ch)

        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()  # remove '('

        else:
            while stack and priority(ch) <= priority(stack[-1]):
                result += stack.pop()
            stack.append(ch)

    while stack:
        result += stack.pop()

    return result


# Main
if __name__ == "__main__":
    expression = "a+b*(c^d-e)"
    ans = infix_to_postfix(expression)
    print("ANS ->", ans)