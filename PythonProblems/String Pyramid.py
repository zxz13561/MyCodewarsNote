def watch_pyramid_from_the_side(characters):
    res = ""
    len_list = [1 + i * 2 for i in range(len(characters))]
    for i, c in enumerate(characters):

    return len_list


if __name__ == '__main__':
    characters = '*#'
    print(watch_pyramid_from_the_side(characters))
