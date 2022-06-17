
def solution(S):
    # write your code in Python 3.6
    stack = []
    if len(S) == 0:
        return 1
    for i in S:
        if i =='{' or i == '(' or i == '[':
            stack.append(i)
        elif i== '}' and len(stack) != 0 and stack.pop() != '{':
            return 0
        elif i== ')' and len(stack) != 0 and stack.pop() != '(':
            return 0
        elif i== ']' and len(stack) != 0 and stack.pop() != '[':
            return 0
    return 1 if len(stack) == 0 else 0