


def hamming(n):
    h = [1] * n
    x2, x3, x5 = 2, 3, 5
    i = j = k = 0

    for n in range(1, n):
        h[n] = min(x2, x3, x5)
        if x2 == h[n]:
            i += 1
            x2 = 2 * h[i]
            print("2 * " + str(h[i]) + " = " + str(x2))
        if x3 == h[n]:
            j += 1
            x3 = 3 * h[j]
            print("3 * " + str(h[j]) + " = " + str(x3))
        if x5 == h[n]:
            k += 1
            x5 = 5 * h[k]
            print("5 * " + str(h[k]) + " = " + str(x5))

    return h[-1]


def mult_res(m, para):
    return (2 ** (m[0] * para)) * (3 ** (m[1] * para)) * (5 ** (m[2] * para))


class test(object):
    def expect(self, check, string):
        return print("pass" if check else string)


if __name__ == '__main__':
    test().expect(hamming(1) == 1, "hamming(1) should be 1")
    test().expect(hamming(2) == 2, "hamming(2) should be 2")
    test().expect(hamming(3) == 3, "hamming(3) should be 3")
    test().expect(hamming(4) == 4, "hamming(4) should be 4")
    test().expect(hamming(5) == 5, "hamming(5) should be 5")
    test().expect(hamming(6) == 6, "hamming(6) should be 6")
    test().expect(hamming(7) == 8, "hamming(7) should be 8")
    test().expect(hamming(8) == 9, "hamming(8) should be 9")
    test().expect(hamming(9) == 10, "hamming(9) should be 10")
    test().expect(hamming(10) == 12, "hamming(10) should be 12")
    test().expect(hamming(11) == 15, "hamming(11) should be 15")
    test().expect(hamming(12) == 16, "hamming(12) should be 16")
    test().expect(hamming(13) == 18, "hamming(13) should be 18")
    test().expect(hamming(14) == 20, "hamming(14) should be 20")
    test().expect(hamming(15) == 24, "hamming(15) should be 24")
    test().expect(hamming(16) == 25, "hamming(16) should be 25")
    test().expect(hamming(17) == 27, "hamming(17) should be 27")
    test().expect(hamming(18) == 30, "hamming(18) should be 30")
    test().expect(hamming(19) == 32, "hamming(19) should be 32")
