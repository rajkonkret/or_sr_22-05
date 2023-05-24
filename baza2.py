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
    addresses = relationship('Address',
                             back_populates='person',
                             order_by="Address.email",
                             cascade='all, delete-orphan')

    def __repr__(self):
        return f'{self.name}(id={self.id})'


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    email = Column(String)
    person_id = Column(ForeignKey('person.id'))
    person = relationship('Person', back_populates='addresses')

    def __str__(self):
        return self.email

    __repr__ = __str__


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
ssesion = Session()
anakin = Person(name='Anakin', age=38)
obi = Person(name="Obi Wan Kenobi", age=40)
obi.addresses = [
    Address(email='obi@exampe.com'),
    Address(email='wanam@example.com')
]

ssesion.add(anakin)
ssesion.add(obi)
ssesion.commit()

all_ = ssesion.query(Person).all()
print(all_)

an1 = ssesion.query(Person).first()
print(an1)
print(type(an1))
print(an1.id, an1.name, an1.age)

obi1 = ssesion.query(Person).filter(
    Person.name.like('Obi%')
).first()

print(obi1)
print(obi1.addresses)