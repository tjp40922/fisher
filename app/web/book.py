from flask import jsonify, request
from app.libs.helper import is_isbn_or_key
from app.spider.yushu_book import YUShuBook
from . import web
from app.forms.book import SearchForm


@web.route('/book/search')
def search():
    """
    :return:
    """
    form = SearchForm(request.args)
    if form.validate():
        q = form.q.data.strip()
        page = form.page.data
        isbn_or_key = is_isbn_or_key(q)
        if isbn_or_key == 'isbn':
            result = YUShuBook.get_by_isbn(q)
        else:
            result = YUShuBook.get_by_keyword(q)
        return jsonify(result)
        # return (json.dumps(result),'200',{'content-type':'application/json'})
    else:
        return jsonify(form.errors)