import unittest
from blackjack import score, stand


class TestScoreFunction(unittest.TestCase):
    def test_1_hand(self):
        test_1 = [3, 12]
        self.assertEqual(score(test_1), (13, 0))

    def test_2_hand(self):
        test_2 = [5, 5, 10]
        self.assertEqual(score(test_2), (20, 0))

    def test_3_hand(self):
        test_3 = [11, 10, 1]
        self.assertEqual(score(test_3), (21, 0))

    def test_4_hand(self):
        test_4 = [1, 5]
        self.assertEqual(score(test_4), (16, 1))

    def test_5_hand(self):
        test_5 = [1, 1, 5]
        self.assertEqual(score(test_5), (17, 1))

    def test_6_hand(self):
        test_6 = [1, 1, 1, 7]
        self.assertEqual(score(test_6), (20, 1))

    def test_7_hand(self):
        test_7 = [7, 8, 10]
        self.assertEqual(score(test_7), (25, 0))

    def test_8_hand(self):
        test_8 = [1, 13]
        self.assertEqual(score(test_8), (21, 1))

    def test_9_hand(self):
        test_9 = [3, 2, 1]
        self.assertEqual(score(test_9), (16, 1))

    def test_10_hand(self):
        test_10 = [11, 1]
        self.assertEqual(score(test_10), (21, 1))

    def test_11_hand(self):
        test_11 = [1, 2, 1]
        self.assertEqual(score(test_11), (14, 1))

    def test_12_hand(self):
        test_11 = [5, 6, 7]
        self.assertEqual(score(test_11), (18, 0))

    def test_13_hand(self):
        test_11 = [6, 2, 7]
        self.assertEqual(score(test_11), (15, 0))

    def test_14_hand(self):
        test_11 = [3, 4, 3, 5]
        self.assertEqual(score(test_11), (15, 0))


class TestStandFunction(unittest.TestCase):
    def test_stand(self):
        stand_boolean = 'soft'
        self.assertTrue(stand(11, stand_boolean, [11, 1]), True)

    def test_stand2(self):
        stand_boolean = 'hard'
        self.assertTrue(stand(16, stand_boolean, [11, 1]), True)

    def test_stand3(self):
        stand_boolean = 'soft'
        self.assertTrue(stand(14, stand_boolean, [9, 1, 1]), True)

    def test_stand4(self):
        stand_boolean = 'hard'
        self.assertFalse(stand(15, stand_boolean, [8, 6]), False)

    def test_stand5(self):
        stand_boolean = 'soft'
        self.assertFalse(stand(15, stand_boolean, [4, 5]), False)

    def test_stand6(self):
        stand_boolean = 'hard'
        self.assertTrue(stand(15, stand_boolean, [4, 5, 5, 3]), True)

    def test_stand7(self):
        stand_boolean = 'soft'
        self.assertTrue(stand(12, stand_boolean, [1, 1]), True)

    def test_stand8(self):
        stand_boolean = 'hard'
        self.assertTrue(stand(18, stand_boolean, [4, 5, 7, 4]), True)

    def test_stand9(self):
        stand_boolean = 'soft'
        self.assertTrue(stand(13, stand_boolean, [1, 5, 1]), True)

    def test_stand10(self):
        stand_boolean = 'hard'
        self.assertTrue(stand(21, stand_boolean, [1, 2, 3, 4, 1]), True)

    def test_stand11(self):
        stand_boolean = 'hard'
        self.assertTrue(stand(16, stand_boolean, [10, 4, 2]), True)

    def test_stand12(self):
        stand_boolean = 'hard'
        self.assertTrue(stand(16, stand_boolean, [1, 3, 2]), True)


if __name__ == '__main__':
    unittest.main()
