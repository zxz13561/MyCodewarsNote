def to_camel_case(text):
    r_word = ''
    first_word = True
    split_list = ['-', '_']
    head = 0
    for i in range(len(text)):
        if text[i] in split_list and first_word:
            r_word += text[0:i]
            head = i + 1
            first_word = False
        elif text[i] in split_list:
            r_word += text[head:i].capitalize()
            head = i + 1
        elif i == len(text) - 1:
            r_word += text[head:i + 1].capitalize()

    return r_word


if __name__ == '__main__':
    input_s = "the-stealth-warrior"
    print(to_camel_case(input_s))
