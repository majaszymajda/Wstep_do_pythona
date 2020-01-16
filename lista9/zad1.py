import numpy 
import unittest


def znajdowanieDET(a):
    return int(numpy.linalg.det(a))



class Tests(unittest.TestCase):
    new_array = [[1, 2, 3], [3, 6, 7], [9, 7,  9]]


    def test_czy_liczby(self):
        for row in self.new_array:
            for col in row:
                """
                try:
                     asser isinstance (col, (int, float)), 'Zly typ danych w macierzy'
                except AssertionError as message:
                    print(message)
                """
                self.assertIsInstance(col, (int, float))

    def  test_czy_zwraca_db(self):
        self.a = numpy.array(self.new_array)
        self.assertAlmostEqual(znajdowanieDET(self.a), -18)


if __name__ == '__main__':
    unittest.main()
