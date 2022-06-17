def order(sentence):
    if sentence == "":
        return sentence

    w_list = sentence.split(' ')
    swap_list = list(w_list)
    w_num = [int(c) for w in w_list for c in w if c.isdigit()]
    re_str = ""
    for i in w_num:
        swap_list[i - 1] = w_list.pop(0)
    return str.join(" ", swap_list)


if __name__ == '__main__':
    input_s1 = "is2 Thi1s T4est 3a"
    input_s2 = "4of Fo1r pe6ople g3ood th5e the2"
    input_s3 = ""

    print(order(input_s1))
    print(order(input_s2))
    print(order(input_s3))
