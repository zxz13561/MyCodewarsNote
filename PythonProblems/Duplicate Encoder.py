from collections import Counter


def duplicate_encode(word):
    word = word.lower()
    count_word = Counter(word)
    ret_string = ""
    for c in list(word):
        ret_string += ")" if count_word[c] > 1 else "("

    return ret_string


if __name__ == '__main__':
    i1 = "din"
    i2 = "recede"
    i3 = "Success"
    i4 = "(( @"

    print(duplicate_encode(i1))
    print(duplicate_encode(i2))
    print(duplicate_encode(i3))
    print(duplicate_encode(i4))

