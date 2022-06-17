def expanded_form(num):
    ten_pow = 1
    nums = []
    temp_num = num
    while 10 ** (ten_pow - 1) < num:
        val = temp_num % 10 ** ten_pow
        if val != 0:
            nums.append(str(val))
            temp_num -= val

        ten_pow += 1

    return str.join(" + ", nums[::-1])


if __name__ == '__main__':
    i1 = 12
    i2 = 42
    i3 = 70304

    print(expanded_form(i1))
    print(expanded_form(i2))
    print(expanded_form(i3))

