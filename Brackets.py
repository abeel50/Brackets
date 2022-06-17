
def solution(S):
    # write your code in Python 3.6
    stack = []
    if len(S) == 0:
        return 1
    for i in S:
        if i =='{' or i == '(' or i == '[':
            stack.append(i)
        elif (i== '}' or i == ')' or i ==']' ) and len(stack) != 0:
            t = stack.pop() + i
            if t!= "()" and t != "{}" and t!= "[]":
                return 0
        else:
            return 0
    return 1 if len(stack) == 0 else 0