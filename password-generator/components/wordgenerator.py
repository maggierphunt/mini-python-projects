from RandomWordGenerator import RandomWord

r = RandomWord()


def random_word():
    word = r.get_random_word()
    length = len(word)

    return word, length


class WordGenerator():

    def words_list_gen(self):

        words_list = []
        l = 0

        while l < 12:
            word = random_word()
            words_list.append(word[0])
            l += word[1]
        print(words_list)
        return words_list
