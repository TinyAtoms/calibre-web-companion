from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
engine = create_engine('sqlite:///C://Users//MassiveAtoms//Documents//Calibre Library//metadata.db.', echo=True)
Base = declarative_base(engine)
########################################################################

class Author(Base): # needed
    """"""
    __tablename__ = 'authors'
    __table_args__ = {'autoload':True}
    # has int id, text name, sort 

class Comment(Base): # needed
    """"""
    __tablename__ = 'comments'
    __table_args__ = {'autoload':True}
    # has int id, int book, text text

# class Data(Base): # maybe
#     """"""
#     __tablename__ = 'data'
#     __table_args__ = {'autoload':True}
#     # has int id, int book, text format, text name

class Identifier(Base): # needed
    """"""
    __tablename__ = 'identifiers'
    __table_args__ = {'autoload':True}
    # has int id, int book, text value

class Publisher(Base): # needed
    """"""
    __tablename__ = 'publishers'
    __table_args__ = {'autoload':True}
    # has int id, text name

class Rating(Base): # needed
    """"""
    __tablename__ = 'ratings'
    __table_args__ = {'autoload':True}
    # has int id,  int rating

class Series(Base): # needed
    """"""
    __tablename__ = 'series'
    __table_args__ = {'autoload':True}
    # has int id,  text name

class Tag(Base): # needed
    """"""
    __tablename__ = 'tags'
    __table_args__ = {'autoload':True}
    # has int id,  text name

class Book(Base): # needed
    """"""
    __tablename__ = 'books'
    __table_args__ = {'autoload':True}
    # has int id,  text title, text sort, time timestamp, time pubdate, 
    # float series_index, text path 

class Book_author_link(Base): # needed
    """"""
    __tablename__ = 'books_authors_link'
    __table_args__ = {'autoload':True}
    # has int id,  id book, id author

class Book_publisher_link(Base): # needed
    """"""
    __tablename__ = 'books_publishers_link'
    __table_args__ = {'autoload':True}
    # has int id,  id book, id publisher

class Book_rating_link(Base): # needed
    """"""
    __tablename__ = 'books_ratings_link'
    __table_args__ = {'autoload':True}
    # has int id,  id book, id rating

class Book_series_link(Base): # needed
    """"""
    __tablename__ = 'books_series_link'
    __table_args__ = {'autoload':True}
    # has int id,  id book, id series

class Book_tags_link(Base): # needed
    """"""
    __tablename__ = 'books_tags_link'
    __table_args__ = {'autoload':True}
    # has int id,  id book, id tag


#----------------------------------------------------------------------
def loadSession():
    """"""
    metadata = Base.metadata
    Session = sessionmaker(bind=engine)
    session = Session()
    return session
    
if __name__ == "__main__":
    session = loadSession()
    res = session.query(Book).all()
    for i in res:
        print(i.id, i.title, i.sort, i.timestamp, i.pubdate, i.series_index, i.path)

