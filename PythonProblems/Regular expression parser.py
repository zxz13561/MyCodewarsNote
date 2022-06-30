"""
This problem has some issue, wait for fix
"""


class RegExp:
    def __init__(self, *args):
        self.args = args

    def __repr__(self):
        args = ", ".join(map(repr, self.args))
        return f"{self.__class__.__name__}({args})"

    def __eq__(self, other):
        return type(self) is type(other) and self.args == other.args


class Any(RegExp):
    pass


class Normal(RegExp):
    pass


class Or(RegExp):
    pass


class Str(RegExp):
    pass


class ZeroOrMore(RegExp):
    pass


# Your task is to build an AST using those nodes.
# See sample tests or test output for examples of usage.

def parse_regexp(indata):
    # Check Valid
    if not indata:
        return None
    elif len(indata) == 1 and (indata[0] in ['(', ')', '*']):
        return None

    count_b, count_total_b, count_or = 0, 0, 0

    for idx, w in enumerate(indata):
        if count_b < 0:
            return None
        elif w == '*' and idx < len(indata) - 1 and indata[idx + 1] == '*':
            return None
        elif w == '(' and idx < len(indata) - 1 and indata[idx + 1] == ')':
            return None
        elif w == '|':
            count_or += 1
        elif w in ['(', ')']:
            count_b += 1 if w == '(' else -1
            count_total_b += 1
            count_or += -1 if count_or >= 1 else 0

    if count_total_b == len(indata) or count_b != 0 or count_or > 1:
        return None

    # Split all to relate class
    all_to_list = []
    for s in indata:
        if s not in ['.', '(', ')', '|', '*']:
            all_to_list.append(Normal(s))
        elif s == '|':
            all_to_list.append(Or())
        elif s == '*':
            all_to_list.append(ZeroOrMore())
        elif s == '.':
            all_to_list.append(Any())
        else:
            all_to_list.append(s)

    # Group Normal by Str
    """

    """
    Str_list = []
    new_list = []
    is_checking = False
    curr_beg, curr_tail = 0, 0
    for idx, ele in enumerate(all_to_list):
        if is_checking and (type(ele) == type(Normal()) or type(ele) == type(Any())):
            Str_list.append(ele)
        elif ele == '(' and not is_checking:
            curr_tail = idx
            new_list += all_to_list[curr_beg:curr_tail+1]
            is_checking = True
            curr_beg = idx
        elif (ele == ')' and is_checking) or (ele == '(' and is_checking):
            new_list.append(Str(Str_list) if len(Str_list) >= 2 else Str_list[0])
            Str_list = []
            is_checking = False
            curr_beg, curr_tail = idx, idx

    new_list += all_to_list[curr_tail:]

    normal_list = []
    for idx, ele in enumerate(all_to_list):
        if type(Normal()) == type(ele) or ele == Any():
            normal_list.append(ele)
        elif (type(Normal()) != type(ele) or ele != Any()) and len(normal_list) == 1:
            new_list.append(normal_list[0])
            new_list.append(ele)
            normal_list = []
        elif (type(Normal()) != type(ele) or ele != Any()) and len(normal_list) > 1:
            new_list.append(Str(normal_list))
            new_list.append(ele)
            normal_list = []
        else:
            new_list.append(ele)

    # check last element
    if normal_list:
        new_list.append(normal_list[0] if len(normal_list) == 1 else Str(normal_list))

    # Check Zero or more
    for idx, ele in enumerate(new_list):
        if type(ele) == type(ZeroOrMore()):
            if type(new_list[idx - 1]) == type(Str()):
                pre_args = new_list[idx - 1].args[0]
                pre_args[-1] = ZeroOrMore(pre_args[-1])
                new_list[idx - 1] = Str(pre_args)
                new_list.pop(idx)
            elif type(new_list[idx - 1]) == type(Normal()):
                new_list[idx - 1] = ZeroOrMore(new_list[idx - 1])
                new_list.pop(idx)

    # Group by basket
    while '(' in new_list or ')' in new_list:
        left_b, right_b, count = 0, 0, 0
        for idx, ele in enumerate(new_list):
            if ele == '(':
                left_b = idx
            elif ele == ')':
                right_b = idx
                break
        mid_idx = (right_b - left_b) // 2 + left_b

        tmp_ele = new_list[mid_idx]
        if right_b - left_b > 3:
            tmp_ele.args = new_list[mid_idx - 1], new_list[mid_idx + 1]

        del new_list[left_b:right_b + 1]
        new_list.insert(left_b, tmp_ele)

    is_finish_loop = True
    count_time = 0
    while len(new_list) > 1:
        count_time += 1
        if count_time >= 500:
            return None
        for idx, ele in enumerate(new_list):
            if type(ele) == type(Or()) and ele.args == ():
                prev_e, next_e = new_list[idx - 1], new_list[idx + 1]
                ele.args = (prev_e, next_e)
                new_list.remove(prev_e)
                new_list.remove(next_e)
                is_finish_loop = False
                break
            elif type(ele) == type(ZeroOrMore()) and ele.args == ():
                new_list.pop(idx)  # Remove element
                new_list[idx - 1] = ZeroOrMore(new_list[idx - 1])
                is_finish_loop = False
                break

        if is_finish_loop and len(new_list) > 1:
            new_list = Str(new_list)
            return new_list

    return new_list[0]


if __name__ == '__main__':
    i_arr = ['((aa)|ab)*|a', '((a.)|.b)*|a', '(ab)*', 'a(b|a)', '*}_8[H^xs6&C<>mq]~VXgT2\x0cjPMlwpUFz\x0bk3', 'l-hLM%?mA\tVc7{g/ax]vq|@&E;jPBy3t=\x0b9ZdfwXpU(H~#>n[0o:sJ64\r$}Wk\n']
    random_i = ['b+6uY8vn(<cAKCGlo_[1/p).@qW,ig$;Isk&P\x0bU4eB2\n%Z \'F^\tdwh->#"y{L\rmD9R7trS!H*xT50', 'hI$HL;vX\t4PS()[l,3}s@/qy<iNeZrmWYz.UVaTO]|2\n=^8tDfQ"%g9c\x0c0d+-:xo{15\'F\x0b>J_&#KpuAG\\ jbw~*?kRM7`!E']
    i = '((a.)|.b)*|a'
    print(parse_regexp(random_i[0]))
