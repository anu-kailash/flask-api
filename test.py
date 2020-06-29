from sqlalchemy.orm import sessionmaker
from sqlalchemy.testing import db

from model import Artists, Album, engine
# create a Session *********
Session = sessionmaker(bind=engine)
session = Session()
# add objects to the table -************
# c1 = Artists(Name='VJ')
# session.add(c1)
# session.commit()
# add objects to the table -************
#Album.Title = 'The Sun Rise',
#Album.ArtistId = 13


# Select the data's in table and printing ---------------Album Table-----------------------------------------------
result = session.query(Album).all()
for row in result:
   print("Title: ",row.Title, "Artist ID :", row.ArtistId)

# Printing a particular row using get(id) ------------------Album Table---------------------------------------------
# x = session.query(Album).get(2)
# print("Title : ", x.Title, "Artist :", x.ArtistId)
# # Select the data's in table and printing ---------------Artists Table-----------------------------------------------
# res = session.query(Artists).all()
# for row in res:
#    print("Artist ID :", row. ArtistId,"Name: ",row.Name)

