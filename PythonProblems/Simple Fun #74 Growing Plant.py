def plant(up, down, t):
    curr1 = up
    curr2 = up
    days = 1
    while curr1 < t:
        print(days, curr1, curr2)
        curr1 -= down
        curr1 += up
        curr2 += up - down
        days += 1

    return days


if __name__ == '__main__':
    print(plant(16, 14, 487))
