import json
from app import *
from model import Artists, Album, engine
result = session.query(Album).all()
for row in result:
    a1=("Title: ", row.Title, "Artist ID :", row.ArtistId)
    print (a1)
data=json.dumps(a1)
print(data)