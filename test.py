import unittest
from sqlalchemy.orm import sessionmaker
from model import engine, Artist, Album

Session = sessionmaker(bind=engine)
session = Session()
session.add_all([
    Album(Title='ABCD-TEST', ArtistId='1'),
    Album(Title='Sundhar', ArtistId='2'),
    Album(Title='Veenapoov', ArtistId='3')]
)

session.commit()


class TestTable(unittest.TestCase):

    def test_data(self):
        artist = Artist(name='Linto')
        session.add(artist)
        session.commit()
        test_value = 'Linto'
        self.assertEqual(artist.name, str(test_value), 'should be name')

    def test_get_value_with_Id(self):
        value = session.query(Album).get(2)
        self.assertEqual({value.Title, value.ArtistId}, {'Sundhar', 2}, 'should be same')
        print({value.Title, value.ArtistId})

    def test_viewAllData(self):
        result = session.query(Album).all()
        for row in result:
            expected_result = {"Title": row.Title, "ArtistId": row.ArtistId}
            self.assertEqual(expected_result, {"Title": row.Title, "ArtistId": row.ArtistId}, "should be same")
            print(expected_result)


if __name__ == '__main__':
    unittest.main()
