from fencer import Fencer, Rank
import unittest

class test_Fencer(unittest.TestCase):
    def compareFields(self, data, expected):
        f = Fencer(*data)
        self.assertEqual(f.lastName, expected[0])
        self.assertEqual(f.firstName, expected[1])
        self.assertEqual(f.school, expected[2])
        self.assertEqual(f.rank.rankLetter, expected[3])
        self.assertEqual(f.rank.rankNumber, expected[4])

    def test_positive(self):
        self.compareFields(('LICHTEN', 'Keith', 'EBFG', 'A15'),('LICHTEN', 'Keith', 'EBFG', 'A', 15))

    def test_noSchool(self):
        self.compareFields(('LICHTEN', 'Keith', '', 'A15'), ('LICHTEN', 'Keith', 'unafilliated', 'A', 15))

    def test_rankU(self):
        self.compareFields(('LICHTEN', 'Keith', 'EBFG', 'U'),('LICHTEN', 'Keith', 'EBFG', 'U',0))

class test_Rank(unittest.TestCase):
    def compareFields(self, data, expected):
        r = Rank(data)
        self.assertEqual((r.rankNumber,r.rankLetter),expected)

    def test_creation(self):
        tests = [('A15',(15 ,'A')),
                 ('U', (0,'U')),
                 ('B0',(0,'B'))]
        for i in tests:
            self.compareFields(*i)

    def test_eq(self):
        self.assertTrue(Rank('A15')==Rank('A15'))
        self.assertTrue(Rank('a15') == Rank('A15'))

    def test_ne(self):
        self.assertTrue(Rank('U') != Rank('A15'))

    def test_lt(self):
        self.assertTrue(Rank('A14')< Rank('A15'))
        self.assertTrue(Rank('B15') < Rank('A15'))
        self.assertTrue(Rank('U') < Rank('C15'))

    def test_le(self):
        self.assertTrue(Rank('A15')<= Rank('A15'))
        self.assertTrue(Rank('a15') <= Rank('A15'))
        self.assertTrue(Rank('A14')<= Rank('A15'))
        self.assertTrue(Rank('B15') <= Rank('A15'))
        self.assertTrue(Rank('U') <= Rank('C15'))

    def test_gt(self):
        self.assertTrue(Rank('A15') > Rank('A14'))
        self.assertTrue(Rank('A15') > Rank('B15'))
        self.assertTrue(Rank('C15') > Rank('U'))

    def test_ge(self):
        self.assertTrue(Rank('A15') >= Rank('A15'))
        self.assertTrue(Rank('a15') >= Rank('A15'))
        self.assertTrue(Rank('A15') >= Rank('A14'))
        self.assertTrue(Rank('A15') >= Rank('B15'))
        self.assertTrue(Rank('C15') >= Rank('U'))