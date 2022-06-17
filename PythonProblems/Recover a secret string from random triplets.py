def recoverSecret(triplets):
    word_list = triplets[0]

    for clue in triplets[1:]:
        check_clue(clue, word_list)

    for clue in triplets:
        check_clue(clue, word_list)

    return str.join('', word_list)


def check_clue(clue, word_list):
    if clue[0]:
        if clue[0] in word_list and clue[1] in word_list:
            c0_i = word_list.index(clue[0])
            c1_i = word_list.index(clue[1])
            if c0_i > c1_i:
                word_list.remove(clue[0])
                word_list.insert(c1_i, clue[0])
        elif clue[0] not in word_list and clue[1] in word_list:
            word_list.insert(word_list.index(clue[1]), clue[0])
        elif clue[0] not in word_list:
            word_list.insert(0, clue[0])

    if clue[1]:
        if clue[1] in word_list and clue[2] in word_list:
            c1_i = word_list.index(clue[1])
            c2_i = word_list.index(clue[2])
            if c1_i > c2_i:
                word_list.remove(clue[1])
                word_list.insert(c2_i, clue[1])
        elif clue[1] not in word_list and clue[2] in word_list:
            word_list.insert(word_list.index(clue[2]), clue[1])
        elif clue[1] not in word_list:
            word_list.insert(1, clue[1])

    if clue[2] not in word_list:
        word_list.append(clue[2])


if __name__ == '__main__':
    i_triplets = [
        ['t', 'u', 'p'],
        ['w', 'h', 'i'],
        ['t', 's', 'u'],
        ['a', 't', 's'],
        ['h', 'a', 'p'],
        ['t', 'i', 's'],
        ['w', 'h', 's']
    ]

    print(recoverSecret(i_triplets))
