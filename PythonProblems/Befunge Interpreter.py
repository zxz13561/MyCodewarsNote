import random

def interpret(code):
    code_list = [[s for s in l] for l in code.split("\n")]
    x, y = -1, 0
    stack_l = []
    output = ""
    directs = {1: [1, 0], 2: [-1, 0], 3: [0, 1], 4: [0, -1]}
    curr_direct = [1, 0]
    asciiEnable = False

    while True:
        x += curr_direct[0]
        y += curr_direct[1]
        sym = code_list[y][x]

        if sym == "\"":
            asciiEnable = False if asciiEnable else True
        elif asciiEnable:
            stack_l.append(ord(sym))
        elif sym == '@':
            break
        elif sym == " ":
            continue
        elif sym.isnumeric():
            stack_l.append(int(sym))
        elif sym == ',':
            output += chr(stack_l.pop(-1)) if stack_l else ""
        elif sym == ".":
            output += str(stack_l.pop(-1)) if stack_l else "0"
        elif sym == "$":
            stack_l.pop(-1)
        elif sym == "#":
            x += curr_direct[0]
            y += curr_direct[1]
        elif sym == ":":
            stack_l.append(stack_l[-1] if stack_l else 0)
        elif sym == "_":
            curr_direct = [1, 0] if stack_l.pop(-1) == 0 else [-1, 0]
        elif sym == "|":
            curr_direct = [0, 1] if stack_l.pop(-1) == 0 else [0, -1]
        elif sym == '>':
            curr_direct = [1, 0]
        elif sym == '<':
            curr_direct = [-1, 0]
        elif sym == '^':
            curr_direct = [0, -1]
        elif sym == 'v':
            curr_direct = [0, 1]
        elif sym == '?':
            d = random.randint(1, 4)
            curr_direct = drection[d]
        elif sym == '+':
            n1, n2 = stack_l.pop(-1), stack_l.pop(-1)
            stack_l.append(n1 + n2)
        elif sym == '-':
            n1, n2 = stack_l.pop(-1), stack_l.pop(-1)
            stack_l.append(n2 - n1)
        elif sym == '*':
            n1, n2 = stack_l.pop(-1), stack_l.pop(-1)
            stack_l.append(n1 * n2)
        elif sym == '/':
            n1, n2 = stack_l.pop(-1), stack_l.pop(-1)
            stack_l.append(n2 // n1 if n1 != 0 else 0)
        elif sym == '%':
            n1, n2 = stack_l.pop(-1), stack_l.pop(-1)
            stack_l.append(n2 % n1 if n1 != 0 else 0)
        elif sym == 'p':
            c_y, c_x, c = stack_l.pop(-1), stack_l.pop(-1), stack_l.pop(-1)
            code_list[c_y][c_x] = chr(c)
        elif sym == 'g':
            c_y, c_x = stack_l.pop(-1), stack_l.pop(-1)
            stack_l.append(ord(code_list[c_y][c_x]))
        elif sym == '!':
            val = stack_l.pop(-1)
            stack_l.append(1 if val == 0 else 0)
        elif sym == '`':
            n1, n2 = stack_l.pop(-1), stack_l.pop(-1)
            stack_l.append(1 if n2 > n1 else 0)
        elif sym == "\\":
            n1, n2 = stack_l.pop(-1), stack_l.pop(-1) if stack_l else 0
            stack_l.append(n1)
            stack_l.append(n2)

    return output


if __name__ == '__main__':
    # input_s = ">987v>.v\nv456<  :\n>321 ^ _@"
    # input_s = ">              v\nv  ,,,,,\"Hello\"<\n>48*,          v\nv,,,,,,\"World!\"<\n>25*,@"
    input_s = "08>:1-:v v *_$.@\n  ^    _$>\:^"
    print(interpret("01->1# +# :# 0# g# ,# :# 5# 8# *# 4# +# -# _@"))
