def zero(operate=None):  # your code here
    return 0 if not operate else run_operate([0] + operate)


def one(operate=None):  # your code here
    return 1 if not operate else run_operate([1] + operate)


def two(operate=None):  # your code here
    return 2 if not operate else run_operate([2] + operate)


def three(operate=None):  # your code here
    return 3 if not operate else run_operate([3] + operate)


def four(operate=None):  # your code here
    return 4 if not operate else run_operate([4] + operate)


def five(operate=None):  # your code here
    return 5 if not operate else run_operate([5] + operate)


def six(operate=None):  # your code here
    return 6 if not operate else run_operate([6] + operate)


def seven(operate=None):  # your code here
    return 7 if not operate else run_operate([7] + operate)


def eight(operate=None):  # your code here
    return 8 if not operate else run_operate([8] + operate)


def nine(operate=None):  # your code here
    return 9 if not operate else run_operate([9] + operate)


def plus(num=None):  # your code here
    return ["+", num]


def minus(num=None):  # your code here
    return ["-", num]


def times(num=None):  # your code here
    return ["*", num]


def divided_by(num=None):  # your code here
    return ["//", num]


def run_operate(op_list):
    if op_list[1] == "+":
        return op_list[0] + op_list[2]
    elif op_list[1] == "-":
        return op_list[0] - op_list[2]
    elif op_list[1] == "*":
        return op_list[0] * op_list[2]
    else:
        return op_list[0] // op_list[2]


if __name__ == '__main__':
    print(eight(minus(three())))
