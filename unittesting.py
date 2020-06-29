import unittest
from sqlalchemy.orm import sessionmaker
from model import engine, Artists, Album
Session = sessionmaker(bind=engine)
session = Session()

class TestTable(unittest.TestCase):
    def test_data(self):
        c1 = Artists(Name='Anuja')
        a1 = Album(Title='My Data', ArtistId=6)
        session.add(c1)
        session.add(a1)
        session.commit()
        self.assertEqual(c1.Name, str('Anuja'), " Should be same")

    def test_view_id(self):
        x = session.query(Album).get(2)
        # print("Title : ", x.Title, "Artist :", x.ArtistId)
        self.assertEqual({x.Title, x.ArtistId}, {'The Bell Jar', 8},"Should be same")

    def test_view(self):
        result = session.query(Album).all()
        for row in result:
            b1 = {"Title " :row.Title, "Artist ID ": row.ArtistId}
            print(b1)
            self.assertEqual(b1,{"Title ":row.Title,"Artist ID ":row.ArtistId } )


if __name__ == '__main__':
    unittest.main()