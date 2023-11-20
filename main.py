from collections import Counter


def get_simbol():
    try:
        with open('text.txt', 'r', encoding="utf-8") as text_file:
            read = text_file.read().lower().replace(' ', '').replace('\n', '')
            all_simbols = len(read)
            c = Counter(read)
            res_freq = {tup[0]: (str(round(int(tup[1])*100/all_simbols, 2))+'%') for tup in c.most_common()}

        # print('Общее количество символов в файле: ', all_simbols)

        for key, value in res_freq.items():
            print("{0}: {1}".format(key, value))

    except FileNotFoundError:
        print('файл не найден')


if __name__ == '__main__':
    get_simbol()
