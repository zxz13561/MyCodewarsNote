def solve_runes(runes):
    digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for s in runes:
        if s.isnumeric() and int(s) in digits:
            digits.remove(int(s))

    for d in digits:
        r_list = runes.replace('?', str(d)).split('=')
        if len(r_list[1]) > 1 and (r_list[1][0] == "0" or r_list[1][0:2] == '-0'):
            continue
        right_val = int(r_list[1])
        left_ans = split_and_cal(r_list[0])
        if right_val == left_ans:
            return d
    return -1


def split_and_cal(r_s):
    nums = []
    temp_n = ""
    ans = 0
    for i, s in enumerate(r_s):
        if s in '+*' or (s == '-' and r_s[i - 1].isnumeric() and i > 0):
            nums.append(int(temp_n))
            nums.append(s)
            temp_n = ""
        else:
            temp_n += s
    nums.append(int(temp_n))

    for i, n in enumerate(nums):
        if n == '+':
            ans += nums[i - 1] + nums[i + 1]
        elif n == '*':
            ans += nums[i - 1] * nums[i + 1]
        elif n == '-':
            ans += nums[i - 1] - nums[i + 1]

    return ans


if __name__ == '__main__':
    # data = "1+1=?"
    # data = "123*45?=5?088"
    # data = "19--45=5?"
    # data = "??*??=302?"
    # data = "?*11=??"
    # data = "-5?*-1=5?"
    # data = "?8?170-1?6256=7?2?14"
    data = "-?56373--9216=-?47157"
    # data = "?*123?45=?"
    print(solve_runes(data))
