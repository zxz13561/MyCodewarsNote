from collections import Counter


def longest(a1, a2):
    return str.join('', sorted((Counter(a1) + Counter(a2)).keys()))


if __name__ == '__main__':
    input_s1 = "xyaabbbccccdefww"
    input_s2 = "xxxxyyyyabklmopq"
    input_s3 = "abcdefghijklmnopqrstuvwxyz"

    print(longest(input_s1, input_s2))
    print(longest(input_s3, input_s3))