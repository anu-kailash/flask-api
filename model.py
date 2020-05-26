from sqlalchemy import create_engine, Column, Integer,NVARCHAR
from sqlalchemy.ext.declarative import declarative_base
engine=create_engine("sqlite:///chinook.db", echo=True)
Base=declarative_base()


class Albums(Base):
    __tablename__ = 'albums'
    AlbumId=Column(Integer,primary_key=True,autoincrement=True, nullable=True)
    Title=Column(NVARCHAR, nullable=True)
    ArtistId=Column(Integer, nullable=True)


Base.metadata.create_all(engine)