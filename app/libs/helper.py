
def is_isbn_or_key(word):
    """
    对于传进来关键字判断是isbn或者书名
    :param word:
    :return:
    ibsn13: 13位纯数字
    isbn10：0-9的数字加一些  '-'
    """
    isbn_or_key = 'key'
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'
    shor_word = word.replace('-', '')
    if len(shor_word) == 10 and shor_word.isdigit():
        isbn_or_key = 'isbn'
    return isbn_or_key
