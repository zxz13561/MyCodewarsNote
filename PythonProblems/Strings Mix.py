from collections import Counter
import re


def mix(s1, s2):
    # data cleaning
    s1 = re.sub('[^a-z]+', '', s1)
    s2 = re.sub('[^a-z]+', '', s2)

    newS1_c = {k: v for k, v in Counter(s1).items() if v > 1}
    newS2_c = {k: v for k, v in Counter(s2).items() if v > 1}
    print(newS1_c)
    print(newS2_c)

    # make list
    ret_list = []
    while newS1_c or newS2_c:
        if newS1_c:
            k, v = newS1_c.popitem()
            if k in list(newS2_c.keys()):
                v2 = newS2_c.pop(k)
                if v > v2:
                    ret_list.append('1:' + ''.join(k for _ in range(v)))
                elif v < v2:
                    ret_list.append('2:' + ''.join(k for _ in range(v2)))
                else:
                    ret_list.append('=:' + ''.join(k for _ in range(v)))
            else:
                ret_list.append('1:' + ''.join(k for _ in range(v)))

        if newS2_c:
            k, v = newS2_c.popitem()
            if k in list(newS1_c.keys()):
                v1 = newS1_c.pop(k)
                if v > v1:
                    ret_list.append('2:' + ''.join(k for _ in range(v)))
                elif v < v1:
                    ret_list.append('1:' + ''.join(k for _ in range(v1)))
                else:
                    ret_list.append('=:' + ''.join(k for _ in range(v)))
            else:
                ret_list.append('2:' + ''.join(k for _ in range(v)))

    # slice and sort
    ret_list = sorted(ret_list, key=lambda x: len(x), reverse=True) + ["end"]
    new_list = []
    s_index = 0
    max_len = max([len(x) for x in ret_list])
    while max_len > 3:
        for i, ele in enumerate(ret_list):
            if len(ele) < max_len:
                new_list += sorted(ret_list[s_index: i])
                s_index = i
                break
        max_len -= 1
        print(new_list)

    return '/'.join(new_list)


if __name__ == '__main__':
    i_s1 = "my&friend&Paul has heavy hats! &"
    i_s2 = "my friend John has many many friends &"

    # print(mix(i_s1, i_s2))
    # print(mix("Are they here", "yes, they are here"))
    print(mix("Sadus:cpms>orqn3zecwGvnznSgacs","MynwdKizfd$lvse+gnbaGydxyXzayp"))
