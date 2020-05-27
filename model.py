import sqlite3

from sqlalchemy import Column, Integer, NVARCHAR, ForeignKey, DATETIME, NUMERIC
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
# Declare mapping ********
Base=declarative_base()
engine=create_engine('sqlite:///chinook.db', echo=True)


class Album(Base):                  # Model class for Album table in chinook database-------------------------------
    __tablename__ = 'albums'
    AlbumId=Column(Integer, primary_key=True,nullable=False, autoincrement=True)
    Title=Column(NVARCHAR(160), nullable=False)
    ArtistId=Column(Integer,ForeignKey('artists.ArtistId'), nullable=False, )


Base.metadata.create_all(engine)


class Artists(Base):                  # Model class for Artists table in chinook database------------------------------
    __tablename__ = 'artists'
    ArtistId=Column(Integer, primary_key=True,nullable=False, autoincrement=True)
    Name=Column(NVARCHAR(120), nullable=False)


Base.metadata.create_all(engine)
# create a Session *********
Session = sessionmaker(bind=engine)
session = Session()
# add objects to the table -************
# c1 = Artists(Name='Veer')
# session.add(c1)
# session.commit()
# Select the data's in table and printing ---------------Album Table-----------------------------------------------
result = session.query(Album).all()
for row in result:
   print("Title: ",row.Title, "Artist ID :", row.ArtistId)

# Printing a particular row using get(id) ------------------Album Table---------------------------------------------
x = session.query(Album).get(2)
print("Title : ", x.Title, "Artist :", x.ArtistId)
# Select the data's in table and printing ---------------Artists Table-----------------------------------------------
res = session.query(Artists).all()
for row in res:
   print("Artist ID :", row. ArtistId,"Name: ",row.Name)


class Employees(Base):              # Model class for Employees table in chinook database-------------------
    __tablename__ = 'employees'
    EmployeeId=Column(Integer, primary_key=True,nullable=False, autoincrement=True)
    LastName=Column(NVARCHAR(20), nullable=False)
    FirstName=Column(NVARCHAR(20), nullable=False)
    Title = Column(NVARCHAR(30))
    ReportsTo = Column(Integer, ForeignKey('employees.EmployeeId'))
    BirthDate = Column(DATETIME)
    HireDate = Column(DATETIME)
    Address = Column(NVARCHAR(70))
    City = Column(NVARCHAR(40))
    State = Column(NVARCHAR(40))
    Country = Column(NVARCHAR(40))
    PostalCode = Column(NVARCHAR(10))
    Phone = Column(NVARCHAR(24))
    Fax = Column(NVARCHAR(24))
    Email = Column(NVARCHAR(60))


Base.metadata.create_all(engine)


class Customers(Base):                      # Model class for Customers table in chinook database-------------------
    __tablename__ = 'customers'
    CustomerID=Column(Integer, primary_key=True,nullable=False, autoincrement=True)
    FirstName=Column(NVARCHAR(40), nullable=False)
    LastName=Column(NVARCHAR(20), nullable=False)
    Company = Column(NVARCHAR(80))
    Address = Column(NVARCHAR(70))
    City = Column(NVARCHAR(40))
    State = Column(NVARCHAR(40))
    Country = Column(NVARCHAR(40))
    Postal_Code = Column(NVARCHAR(10))
    Phone = Column(NVARCHAR(24))
    Fax = Column(NVARCHAR(24))
    Email = Column(NVARCHAR(60), nullable=False)
    SupportRepId = Column(Integer,ForeignKey('employees.EmployeeId'),nullable=False)


Base.metadata.create_all(engine)


class Genres(Base):                  # Model class for Genres table in chinook database------------------------------
    __tablename__ = 'genres'
    GenreId=Column(Integer, primary_key=True,nullable=False, autoincrement=True)
    Name=Column(NVARCHAR(120), nullable=False)


Base.metadata.create_all(engine)


class MediaTypes(Base):                  # Model class for Media_types table in chinook database-------------------
    __tablename__ = 'media_types'
    MediaTypeId=Column(Integer, primary_key=True,nullable=False, autoincrement=True)
    Name=Column(NVARCHAR(120))


Base.metadata.create_all(engine)


class Tracks(Base):                  # Model class for Tracks table in chinook database-------------------
    __tablename__ = 'tracks'
    TrackId=Column(Integer, primary_key=True,nullable=False, autoincrement=True)
    Name=Column(NVARCHAR(200), nullable=False)
    AlbumId=Column(Integer, ForeignKey('albums.AlbumId'))
    MediaTypeId = Column(Integer, ForeignKey('media_types.MediaTypeId'), nullable=False)
    GenreId = Column(Integer, ForeignKey('genres.GenreId'))
    Composer=Column(NVARCHAR(220))
    Milliseconds=Column(Integer, nullable=False)
    Bytes=Column(Integer)
    UnitPrice=Column(NUMERIC(10,2),nullable=False)


Base.metadata.create_all(engine)