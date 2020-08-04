from django.test import Client, TestCase
from pprint import pprint
from django.test.utils import setup_test_environment
from .models import Book, Author, Publisher, Series, Rating, Tag, Identifier
from django.db.models import Count


client = Client()
client.login(username="testuser", password="dumbeasypassword")

def booklisttest():
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    res = c.get("/books/")
    assert res.status_code == 200
    context = dict(res.context)
    assert sorted(context["book_list"], key=lambda x: x.id)== sorted(Book.objects.all(), key=lambda x: x.id)

def authorlisttest():
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    res = c.get("/authors/")
    assert res.status_code == 200
    context = dict(res.context)
    assert sorted(context["author_list"], key=lambda x: x.id)== sorted(Author.objects.all(), key=lambda x: x.id)


def publisherlisttest():
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    res = c.get("/publishers/")
    assert res.status_code == 200
    context = dict(res.context)
    assert sorted(context["publisher_list"], key=lambda x: x.id)== sorted(Publisher.objects.all(), key=lambda x: x.id)

def serieslisttest():
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    res = c.get("/series/")
    assert res.status_code == 200
    context = dict(res.context)
    assert sorted(context["series_list"], key=lambda x: x.id)== sorted(Series.objects.all(), key=lambda x: x.id)


def ratinglisttest():
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    res = c.get("/ratings/")
    assert res.status_code == 200
    context = dict(res.context)
    assert sorted(context["rating_list"], key=lambda x: x.id)== sorted(Rating.objects.all(), key=lambda x: x.id)

def taglisttest():
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    res = c.get("/tags/")
    assert res.status_code == 200
    context = dict(res.context)
    assert sorted(context["tag_list"], key=lambda x: x.id)== sorted(Tag.objects.all(), key=lambda x: x.id)


def bookdetailtest():
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    ids = [i.id for i in Book.objects.all()][:10]
    for i in ids:
        res = c.get(f"/book/{i}")
        assert res.status_code == 200
        context = dict(res.context)
        assert context["book"] == Book.objects.get(id=i)


def authordetailtest():
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    ids = [i.id for i in Author.objects.all()][:10]
    for i in ids:
        res = c.get(f"/author/{i}")
        assert res.status_code == 200
        context = dict(res.context)
        assert context["author"] == Author.objects.get(id=i)

def publisherdetailtest():
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    ids = [i.id for i in Publisher.objects.all()][:10]
    for i in ids:
        res = c.get(f"/publisher/{i}")
        assert res.status_code == 200
        context = dict(res.context)
        assert context["publisher"] == Publisher.objects.get(id=i)

def seriesdetailtest():
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    ids = [i.id for i in Series.objects.all()][:10]
    for i in ids:
        res = c.get(f"/series/{i}")
        assert res.status_code == 200
        context = dict(res.context)
        assert context["series"] == Series.objects.get(id=i)

def ratingdetailtest():
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    ids = [i.id for i in Rating.objects.all()][:10]
    for i in ids:
        res = c.get(f"/rating/{i}")
        assert res.status_code == 200
        context = dict(res.context)
        assert context["rating"] == Rating.objects.get(id=i)        


def tagdetailtest():
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    ids = [i.id for i in Tag.objects.all()][:10]
    for i in ids:
        res = c.get(f"/tag/{i}")
        assert res.status_code == 200
        context = dict(res.context)
        assert context["tag"] == Tag.objects.get(id=i) 


def search_partial(key, value, book=None):
    c = Client()
    c.login(username="testuser", password="dumbeasypassword")
    res = c.get("/results/", {key : value})
    if not book:
        return dict(res.context)["book_list"]
    return book in dict(res.context)["book_list"]


def searchtest():
    books = [i for i in Book.objects.all()][:10]
    for i in books:
        assert search_partial("title", i.title, i)
        assert search_partial("generic", i.title, i)
        assert search_partial("author", i.author_sort, i)
        author = i.authors.first()
        if author:
            assert search_partial("author", author.name, i)
            assert search_partial("generic", author.name, i)

        assert search_partial("generic", i.author_sort, i)
        id = Identifier.objects.filter(book=i.id).first()
        if id:
            assert search_partial("identifier", id, i)
            assert search_partial("generic", id, i)


    

booklisttest()
bookdetailtest()
authorlisttest()
authordetailtest()
publisherdetailtest()
publisherlisttest()
seriesdetailtest()
serieslisttest()
ratingdetailtest()
ratinglisttest()
tagdetailtest()
taglisttest()
searchtest()