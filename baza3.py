from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine("sqlite:///:memory:")
Base = declarative_base()


class Author(Base):
    __tablename__ = "authors"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship('Book', back_populates='author')


class Publisher(Base):
    __tablename__ = "publishers"
    id = Column(Integer, primary_key=True)
    name = Column(String)

    books = relationship('Book', back_populates='publisher')


class Book(Base):
    __tablename__ = "books"
    id = Column(Integer, primary_key=True)
    title = Column(String)
    author_id = Column(Integer, ForeignKey('authors.id'))
    publisher_id = Column(Integer, ForeignKey('publishers.id'))

    author = relationship("Author", back_populates='books')
    publisher = relationship("Publisher", back_populates='books')


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

new_author = Author(name='Jan Kowalski')
new_publisher = Publisher(name="Wydawnictwo XYZ")
new_book = Book(title="Ksiązka 1", author=new_author, publisher=new_publisher)
session.add_all(
    [new_author, new_publisher, new_book]
)

session.commit()

authors = session.query(Author).all()
publishers = session.query(Publisher).all()
print(authors)
for author in authors:
    print(f"Author: {author.name}")
    for b in author.books:
        print(f"Ksiązka {b.title}, Wydawca {b.publisher.name}")

for publisher in publishers:
    print(f"Wydawca {publisher.name}")
