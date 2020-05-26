from sqlalchemy import Column, Integer, NVARCHAR, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
Base=declarative_base()
engine=create_engine('sqlite:///chinook.db', echo=True)


class Album(Base):
    __tablename__ = 'albums'
    AlbumId=Column(Integer, primary_key=True,nullable=True, autoincrement=True)
    Title=Column(NVARCHAR(160), nullable=True)
    ArtistId=Column(Integer,ForeignKey('artists.ArtistId'), nullable=True, )


Base.metadata.create_all(engine)


class Artists(Base):
    __tablename__ = 'artists'
    ArtistId=Column(Integer, primary_key=True,nullable=True, autoincrement=True)
    Name=Column(NVARCHAR(120), nullable=True)


Base.metadata.create_all(engine)

Session = sessionmaker(bind = engine)
session = Session()
#c1 = Artists(Name = 'Vaishya')

#session.add(c1)
#session.commit()
result = session.query(Album).all()
for row in result:
   print ("Title: ",row.Title, "Artist ID:",row.ArtistId)