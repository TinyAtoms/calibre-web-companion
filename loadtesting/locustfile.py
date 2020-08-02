from locust import HttpUser, task, between
import random
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import json

# -------------------------------- fetching data to test with

with open("./../CalibreWebCompanion/settings.json", "r") as jfile:
    calpath = json.load(jfile)["CALIBRE_DIR"] + "/metadata.db"

with open("dummyusers.json", "r") as jfile:
    users = json.load(jfile)

engine = create_engine(f'sqlite:///{calpath}')
Base = declarative_base(engine)


class Author(Base):  # needed
    """"""
    __tablename__ = 'authors'
    __table_args__ = {'autoload': True}
    # has int id, text name, sort


class Identifier(Base):  # needed
    """"""
    __tablename__ = 'identifiers'
    __table_args__ = {'autoload': True}
    # has int id, int book, text value


class Publisher(Base):  # needed
    """"""
    __tablename__ = 'publishers'
    __table_args__ = {'autoload': True}
    # has int id, text name


class Rating(Base):  # needed
    """"""
    __tablename__ = 'ratings'
    __table_args__ = {'autoload': True}
    # has int id,  int rating


class Series(Base):  # needed
    """"""
    __tablename__ = 'series'
    __table_args__ = {'autoload': True}
    # has int id,  text name


class Tag(Base):  # needed
    """"""
    __tablename__ = 'tags'
    __table_args__ = {'autoload': True}
    # has int id,  text name


class Book(Base):  # needed
    """"""
    __tablename__ = 'books'
    __table_args__ = {'autoload': True}
    # has int id,  text title, text sort, time timestamp, time pubdate,
    # float series_index, text path


def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session


session = loadSession()

titles = [i.title for i in session.query(Book).all()]
authors = [i.name for i in session.query(Author).all()]
identifiers = [i.val for i in session.query(Identifier).all()]
book_ids = [i.id for i in session.query(Book).all()]
author_ids = [i.id for i in session.query(Author).all()]
publisher_ids = [i.id for i in session.query(Publisher).all()]
rating_ids = [i.id for i in session.query(Rating).all()]
series_ids = [i.id for i in session.query(Series).all()]
tag_ids = [i.id for i in session.query(Tag).all()]


def randlist(mylist):
    return mylist[random.randint(0, len(mylist) - 1)]


class UserBehavior(HttpUser):
    wait_time = between(1, 5)

    def on_start(self):
        """ on_start is called when a Locust start before any task is scheduled """
        r = self.client.get('/accounts/login/')
        self.client.headers['Referer'] = self.client.base_url
        user = randlist(users)
        self.client.post('/accounts/login/',
                         {
                             "username": user["user"],
                             "password": user["pw"],
                             'csrfmiddlewaretoken': r.cookies["csrftoken"]
                         })

    @task(1)
    def search_by_title(self):
        title = randlist(titles)
        self.client.get(f"/results/?title={title}", name="search_by_title")

    @task(1)
    def booklist(self):
        self.client.get("/books/")

    @task(1)
    def bookdetail(self):
        pk = randlist(book_ids)
        self.client.get(f"/book/{pk}", name="/book/<id>")

    @task(1)
    def search_by_author(self):
        author = randlist(authors)
        self.client.get(f"/results/?author={author}", name="search_by_author")

    @task(1)
    def authorlist(self):
        self.client.get("/authors/")

    @task(1)
    def authordetail(self):
        pk = randlist(author_ids)
        self.client.get(f"/author/{pk}", name="/author/<id>")

    @task(1)
    def search_by_id(self):
        id_ = randlist(identifiers)
        self.client.get(f"/results/?identifier={id_}", name="search_by_identifier")

    @task(1)
    def search_generic(self):
        t = random.randint(0, 3)
        if not t:
            term = randlist(titles)
        elif t == 1:
            term = randlist(authors)
        else:
            term = randlist(identifiers)
        self.client.get(f"/results/?generic={term}", name="search_generic")

    @task(1)
    def searchbad(self):
        self.client.get("/search/")

    @task(1)
    def ratingslist(self):
        self.client.get("/ratings/")

    @task(1)
    def ratingdetail(self):
        pk = randlist(rating_ids)
        self.client.get(f"/rating/{pk}", name="/rating/<id>")

    @task(1)
    def taglist(self):
        self.client.get("/tags/")

    @task(1)
    def tagdetail(self):
        pk = randlist(tag_ids)
        self.client.get(f"/tag/{pk}", name="/tag/<id>")

    @task(1)
    def serieslist(self):
        self.client.get("/series/")

    @task(1)
    def publisherlist(self):
        self.client.get("/publishers/")

    @task(1)
    def publisherdetail(self):
        pk = randlist(publisher_ids)
        self.client.get(f"/publisher/{pk}", name="/publisher/<id>")
