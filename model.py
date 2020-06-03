from sqlalchemy import Column, Integer, NVARCHAR, ForeignKey, DATETIME, NUMERIC, TEXT
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


class Invoices(Base):                  # Model class for Invoices table in chinook database-------------------
    __tablename__ = 'invoices'
    InvoiceId=Column(Integer, primary_key=True,nullable=False, autoincrement=True)
    CustomerId=Column(Integer,ForeignKey('customers.CustomerID'), nullable=False)
    InvoiceDate = Column(DATETIME, nullable=False)
    BillingAddress = Column(NVARCHAR(70))
    BillingCity = Column(NVARCHAR(40))
    BillingState = Column(NVARCHAR(40))
    BillingCountry = Column(NVARCHAR(40))
    BillingPostalCode = Column(NVARCHAR(10))
    Total = Column(NUMERIC(10,2), nullable=False)


Base.metadata.create_all(engine)


class Invoice_Items(Base):                  # Model class for Invoice_Items table in chinook database-------------------
    __tablename__ = 'invoice_items'
    InvoiceLineId=Column(Integer, primary_key=True,nullable=False, autoincrement=True)
    InvoiceId=Column(Integer,ForeignKey('invoices.InvoiceId'), nullable=False)
    TrackId = Column(Integer,ForeignKey('tracks.TrackId'), nullable=False)
    UnitPrice = Column(NUMERIC(10,2),nullable=False)
    Quantity = Column(Integer,nullable=False)


Base.metadata.create_all(engine)


class Playlists(Base):                  # Model class for Playlists table in chinook database-------------------
    __tablename__ = 'playlists'
    PlaylistId=Column(Integer, primary_key=True,nullable=False, autoincrement=True)
    Name=Column(NVARCHAR(120))


Base.metadata.create_all(engine)


class PlaylistTrack(Base):                  # Model class for PlaylistTrack table in chinook database-------------------
    __tablename__ = 'playlist_track'
    PlaylistId=Column(Integer, ForeignKey('playlists.PlaylistId'),primary_key=True,nullable=False,)
    TrackId=Column(Integer,ForeignKey('tracks.TrackId'),nullable=False)


Base.metadata.create_all(engine)


class SqliteSeq(Base):              # Model class for SqliteSequence table in chinook database------------
    __tablename__='sqliteseq'
    SqliteSeq_Id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    Name = Column(NVARCHAR(40), nullable=True)
    Seq = Column(NVARCHAR(120))


Base.metadata.create_all(engine)


class SqliteStat(Base):         # Model class for SqliteStatic1 table in chinook database------------
    __tablename__='sqlitestatic1'
    SqliteStat_Id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    tbl = Column(TEXT)
    idx = Column(TEXT)
    stat = Column(TEXT)


Base.metadata.create_all(engine)





