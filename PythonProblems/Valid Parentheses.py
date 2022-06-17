from collections import Counter


def valid_parentheses(string):
    if len(string) == 0:
        return True

    check_l = []
    for s in string:
        if s == '(':
            check_l.append(s)
        elif s == ')':
            if len(check_l) >= 1:
                check_l.pop()
            else:
                return False

    return not check_l


if __name__ == '__main__':
    i1 = "()"
    i2 = ")(()))"
    i3 = "("
    i4 = "(())((()())())"
    i5 = "  ("

    print(valid_parentheses(i1))
    print(valid_parentheses(i2))
    print(valid_parentheses(i3))
    print(valid_parentheses(i4))
    print(valid_parentheses(i5))
