from app.libs.httper import Http


class YUShuBook:
    isbn_url = 'http://book.feelyou.top/isbn/{}'
    keyword_url = 'https://book.feelyou.top/search/{}'

    @classmethod
    def get_by_isbn(cls, isbn):
        url = cls.isbn_url.format(isbn)
        result = Http.get(url)
        return result

    @classmethod
    def get_by_keyword(cls, keyword):
        url = cls.keyword_url.format(keyword)
        result = Http.get(url)
        return result
