from math import sqrt


def find_next_square(sq):
    if not sqrt(sq).is_integer():
        return -1
    else:
        return (sqrt(sq) + 1) ** 2


if __name__ == '__main__':
    input_s1 = 121
    input_s2 = 256
    input_s3 = 114

    print(find_next_square(input_s1))
    print(find_next_square(input_s2))
    print(find_next_square(input_s3))