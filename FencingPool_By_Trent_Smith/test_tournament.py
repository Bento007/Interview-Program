from tournament import Tournament, Pool
import unittest

class test_Tournament(unittest.TestCase):

    def setUp(self):
        self.t = Tournament("MEconflicts.csv")
        self.t.create()

    def test_participants(self):
        self.assertEqual(len(self.t.participants) ,24)

    def test_poolMax(self):
        self.assertEqual(self.t.poolMax, 6)

    def test_poolCount(self):
        self.assertEqual(self.t.poolCount, 4)

    def test_poolsLen(self):
        self.assertEqual(len(self.t.pools), 4)

    def test_poolContEqpoolsLen(self):
        self.assertEqual(len(self.t.pools), self.t.poolCount)

    def test_schoolPoolMax(self):
        self.assertEqual(self.t.schoolPoolMax['EBFG'],2)
        self.assertEqual(self.t.schoolPoolMax['NO FEAR'], 2)
        self.assertEqual(self.t.schoolPoolMax['LOUISVLLE F.C.'], 1)
        self.assertEqual(self.t.schoolPoolMax['MEDEO F.C.'], 1)
        self.assertEqual(self.t.schoolPoolMax['OLYMPIANFC / USMPENT'], 1)
        self.assertEqual(self.t.schoolPoolMax['METRO TACOMA'], 1)
        self.assertEqual(self.t.schoolPoolMax['FISHKILL / CANDLE'], 1)
        self.assertEqual(self.t.schoolPoolMax['unafilliated'], 5)

    def test_pools(self):
        for i in self.t.pools:
            self.assertIn(i.poolSize,[5,6])
            for key in i.schools:
                self.assertLessEqual(i.schools[key], self.t.schoolPoolMax[key])

    def test__calculatePoolSize(self):
        self.t.participants = [x for x in range(12)]
        self.t._calculatePoolSize()
        self.assertEqual(self.t.poolCount,2)
        self.assertEqual(self.t.poolMax, 6)

        self.t.participants = [x for x in range(13)]
        self.t._calculatePoolSize()
        self.assertEqual(self.t.poolCount,2)
        self.assertEqual(self.t.poolMax, 7)

        self.t.participants = [x for x in range(16)]
        self.t._calculatePoolSize()
        self.assertEqual(self.t.poolCount,2)
        self.assertEqual(self.t.poolMax, 8)

        self.t.participants = [x for x in range(17)]
        self.t._calculatePoolSize()
        self.assertEqual(self.t.poolCount,3)
        self.assertEqual(self.t.poolMax, 6)




