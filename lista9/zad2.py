import numpy as np
import scipy
from scipy import linalg
import unittest


def metodaLU(a):
    P, L, U = linalg.lu(a)
    return P, L, U


def znajdowanieDET(a):
    return np.linalg.det(a)


class Tests(unittest.TestCase):
    new_mac = [[1, -1, 2], [3, 0, -4], [2, 3, 5]]
    a = np.array(new_mac)

    def test_czy_liczb(self):
        for row in self.new_mac:
            for col in row:
                """
                try:
                     asser isinstance (col, (int, float)), 'Zly typ danych w macierzy'
                except AssertionError as message:
                    print(message)
                """
                self.assertIsInstance(col, (int, float))

    def test_rozmiaru(self):
        col_counter = 0
        row_counter = 0
        for row in self.new_mac:
            for col in row:
                col_counter +=1
            row_counter +=1
        self.assertEqual(col_counter/row_counter, row_counter)

    def testDET(self):
        normal_det = znajdowanieDET(self.a)
        self.assertAlmostEqual (normal_det, 53)

    def testDET_LU(self):
        P, L, U = metodaLU(self.a)
        print('macierze P, L , U: ')
        print('------------------------')
        print(P)
        print('------------------------')
        print(L)
        print('------------------------')
        print(U)
        print('------------------------')
        normal_det = znajdowanieDET(self.a)
        LU_DEt = znajdowanieDET(P)*znajdowanieDET(L)*znajdowanieDET(U)
        print('det(a) ={}' .format(normal_det))
        print('det(a) = det(P*L*U) = det(P)*det(L)*det(U)')
        print('det(p): {}'.format(znajdowanieDET(P)))
        print('* det(l): {} '.format(znajdowanieDET(L)))
        print ('*det(U): {}'.format(znajdowanieDET(U)))
        print('= det{}'.format(LU_DEt))
        self.assertAlmostEqual(normal_det, LU_DEt)

if __name__ == '__main__':
    unittest.main()
