def justify(text, width):
    words = [w + ' ' for w in text.split(' ')]
    len_of_words = [len(w) for w in words]
    temp_list = []
    res = ""
    count = 0
    index = 1

    for w, l in zip(words, len_of_words):
        temp_list += [w]
        count += l
        if count == width + 1:

            print(index, len(str.join("", temp_list)[:-1] + "\\n"))
            index += 1

            res += str.join("", temp_list)[:-1] + "\\n"
            temp_list = []
            count = 0

        elif count == width:
            real_len = count - 1
            space_i = 1
            while real_len < width:
                temp_list.insert(space_i, " ")
                real_len += 1
                space_i += 1

            print(index, len(str.join("", temp_list)[:-1] + "\\n"))
            index += 1

            res += str.join("", temp_list)[:-1] + "\\n"
            temp_list = []
            count = 0

        elif count >= width + 2:
            chose_words = temp_list[:-1]
            real_len = count - l
            loop_index = 0
            if len(chose_words) > 1:
                while real_len - 1 <= width:
                    if loop_index == len(chose_words) - 1:
                        loop_index = 0
                    else:
                        chose_words[loop_index] += " "
                        loop_index += 1
                        real_len += 1

            print(index, len(str.join("", chose_words)[:-1] + "\\n"))
            index += 1

            res += str.join("", chose_words)[:-1] + "\\n"
            temp_list = [w]
            count = l

    if temp_list:
        print(index, str.join("", temp_list)[:-1])
        res += str.join("", temp_list)[:-1]
        return res
    else:
        return res[:-2]


if __name__ == '__main__':
    print(justify('Lorem ipsum dolor sit amet, consectetur adipiscing elit. Vestibulum sagittis dolor mauris, '
                  'at elementum ligula tempor eget. In quis rhoncus nunc, at aliquet orci. Fusce at dolor sit amet '
                  'felis suscipit tristique. Nam a imperdiet tellus. Nulla eu vestibulum urna. Vivamus tincidunt '
                  'suscipit enim, nec ultrices nisi volutpat ac. Maecenas sit amet lacinia arcu, non dictum justo. '
                  'Donec sed quam vel risus faucibus euismod. Suspendisse rhoncus rhoncus felis at fermentum. Donec '
                  'lorem magna, ultricies a nunc sit amet, blandit fringilla nunc. In vestibulum velit ac felis '
                  'rhoncus pellentesque. Mauris at tellus enim. Aliquam eleifend tempus dapibus. Pellentesque '
                  'commodo, nisi sit amet hendrerit fringilla, ante odio porta lacus, ut elementum justo nulla et '
                  'dolor.', 15))
