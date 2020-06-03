from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///chinook.db', echo=True)
Base = declarative_base()
Session = sessionmaker(bind = engine)
session = Session()


class Album(Base):
    __tablename__ = 'albums'
    AlbumId = Column(Integer, nullable=True, primary_key=True, autoincrement=True)
    Title = Column(String(160), nullable=True)
    ArtistId = Column(Integer, nullable=True)


Base.metadata.create_all(engine)
session.add_all([
   Album(Title='ABCD-TEST', ArtistId='1'),
   Album(Title='Sundhar', ArtistId='2'),
   Album(Title='Veenapoov', ArtistId='3')]
)
session.commit()
result=session.query(Album).all()
for row in result:
    print("Title: ", row.Title,"ArtistId: ", row.ArtistId)




class Artist(Base):
    __tablename__ = 'artists'
    ArtistId = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    name = Column(String(120))


Base.metadata.create_all(engine)

class Employee(Base):
    __tablename__ = 'employees'
    EmployeeId = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    FirstName = Column(String(20), nullable=True)
    LastName = Column(String(20), nullable=True)
    Title = Column(String(30))
    ReportsTo = Column(Integer)
    BirthDate = Column(String)
    HireDate = Column(String)
    Address = Column(String(70))
    City = Column(String(40))
    State = Column(String(40))
    Country = Column(String(40))
    PostalCode = Column(String(10))
    Phone = Column(String(24))
    Fax = Column(String(24))
    Email = Column(String(60), nullable=True)


Base.metadata.create_all(engine)


class Customer(Base):
    __tablename__ = 'customers'
    CustomerId = Column(Integer, primary_key=True, nullable=True, autoincrement=True)
    FirstName = Column(String(40), nullable=True)
    LastName = Column(String(20), nullable=True)
    Company = Column(String(80), nullable=True)
    Address = Column(String(70))
    City = Column(String(40))
    State = Column(String(40))
    Country = Column(String(40))
    PostalCode = Column(String(10))
    Phone = Column(String(24))
    Fax = Column(String(24))
    Email = Column(String(60), nullable=True)
    SupportRepId = Column(Integer, ForeignKey('employees.EmployeeId'), nullable=False)


Base.metadata.create_all(engine)


class Genres(Base):
    __tablename__ = 'genres'
    GenreId=Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Name=Column(String(120), nullable=False)


Base.metadata.create_all(engine)


class MediaTypes(Base):
    __tablename__ = 'media_types'
    MediaTypeId = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Name = Column(String(120))


Base.metadata.create_all(engine)