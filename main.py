from collections import Counter


def get_simbol():
    """Метод нахождения символов в файловом документе"""
    try:
        """Блок нахождения файла, открытия и анализа поиска символов"""
        with open('text.txt', 'r', encoding="utf-8") as text_file:
            # "в переменную read помещаем открытый файл чтения, убрав из него все пробелы и переносы строк"
            read = text_file.read().lower().replace(' ', '').replace('\n', '')
            # "все символы равняются длине полученного открытого файла чтения "
            all_simbols = len(read)
            # "переменная с - счетчик для частоты каждого символа в файле"
            count = Counter(read)
            # "переменная res_freq - словарь из ключа-символа и значения-количество частоты в файле"
            res_freq = {tup[0]: (str(round(int(tup[1])*100/all_simbols, 2))+'%') for tup in count.most_common()}

        # print('Общее количество символов в файле: ', all_simbols)

        for key, value in res_freq.items():
            print("{0}: {1}".format(key, value))

    except FileNotFoundError:
        """Блок ошибки нахождения файла"""
        print('файл не найден')


if __name__ == '__main__':
    get_simbol()
