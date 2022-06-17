from collections import OrderedDict


def order_weight(strng):
    if strng == "":
        return strng

    sort_dic = {}
    for num_s in strng.split(' '):
        v = sum([int(c) for c in num_s])
        if v not in sort_dic:
            sort_dic[v] = [num_s]
        else:
            sort_dic[v].append(num_s)

    ret_list = []
    for val in sorted(sort_dic):
        ret_list += sorted(sort_dic[val])

    return str.join(' ', ret_list)


def one_liner(_str):
    return ' '.join(sorted(sorted(_str.split(' ')), key=lambda x: sum(int(c) for c in x)))


if __name__ == '__main__':
    # i_string = "56 65 74 100 99 68 86 180 90"
    # "100 180 90 56 65 74 68 86 99"

    i_string = "2000 10003 1234000 44444444 9999 11 11 22 123"

    print(one_liner(i_string))
