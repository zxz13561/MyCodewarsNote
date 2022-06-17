import re
from collections import Counter


def top_3_words(text):
    text = re.findall("[a-zA-Z][a-zA-Z']+", text.lower())
    count_text = Counter(text)
    keys = sorted(count_text, key=lambda x: count_text[x], reverse=True)
    return keys[0: 3 if len(keys) >= 3 else len(keys)]


if __name__ == '__main__':
    i1 = "In a village of La Mancha, the name of which I have no desire to call to \
        mind, there lived not long since one of those gentlemen that keep a lance \
        in the lance-rack, an old buckler, a lean hack, and a greyhound for \
        coursing. An olla of rather more beef than mutton, a salad on most \
        nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra \
        on Sundays, made away with three-quarters of his income."
    i2 = "  , e   .. "
    i3 = "e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"
    i4 = "  //wont won't won't"
    i5 = "''' ''' ' ''"

    print(top_3_words(i1))
    print(top_3_words(i2))
    print(top_3_words(i3))
    print(top_3_words(i4))
    print(top_3_words(i5))
