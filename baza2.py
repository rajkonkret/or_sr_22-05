from sqlalchemy import (
    Column, Integer, String, ForeignKey, create_engine
)
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///:memory:')
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return f'{self.name}(id={self.id})'


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
ssesion = Session()
anakin = Person(name='Anakin', age=38)
obi = Person(name="Obi Wan Kenobi", age=40)

ssesion.add(anakin)
ssesion.add(obi)
ssesion.commit()

all = ssesion.query(Person).all()
print(all)

an1 = ssesion.query(Person).first()
print(an1)
print(type(an1))
print(an1.id, an1.name, an1.age)

obi1 = ssesion.query(Person).filter(
    Person.name.like('Obi%')
).first()

print(obi1)
