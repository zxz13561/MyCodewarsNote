def decode(s):
    encode_s = 'abdhpF,82QsLirJejtNmzZKgnB3SwTyXG ?.6YIcflxVC5WE94UA1OoD70MkvRuPqH'
    bypass_s = "!@#$%^&*()_+-"
    output = ""

    for i, w in enumerate(s):
        if w not in bypass_s:
            w_i = encode_s.index(w) - i - 1
            ori_w = encode_s[w_i if w_i >= -len(encode_s) else w_i + len(encode_s)]
            output += ori_w
        else:
            output += w

    return output


if __name__ == '__main__':
    # i_s = "atC5kcOuKAr!"
    # i_s = 'Hello World!'
    i_s = "The PRicM brOwn fOx jRmped Oker theGfazTGdekefOper?"
    print(decode("atC5kcOuKAr"))
