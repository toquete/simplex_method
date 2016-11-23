import unittest

from simplex import simplex


class SimplexTest(unittest.TestCase):

    # @unittest.skip("")
    def test_one(self):
        func = [4, 1, 1]

        sa = [
            { 'type': 'e', 'idx': [2.0, 1.0, 2.0], 'z': 4.0},
            { 'type': 'e', 'idx': [3.0, 3.0, 1.0], 'z': 3.0}
        ]

        result, x = simplex(func, sa)

        self.assertAlmostEqual(x, 2.2)

        expected = [0, 0.4, 1.8]
        
        for i, x in enumerate(result):
            self.assertAlmostEqual(x, expected[i])

    # @unittest.skip("")
    # def test_two(self):
    #     func = [-6, 1]

    #     sa = [
    #         { 'type': 'le', 'idx': [4.0, 1.0], 'z': 21.0},
    #         { 'type': 'ge', 'idx': [2.0, 3.0], 'z': 13.0},
    #         { 'type': 'e', 'idx': [-1.0, 1.0], 'z': 1.0},
    #     ]

    #     result, x = simplex(func, sa)

    #     self.assertAlmostEqual(x, -19)

    #     expected = [4, 5]
        
    #     for i, x in enumerate(result):
    #         self.assertAlmostEqual(x, expected[i])

    # # @unittest.skip("")
    # def test_lista1(self):
    #     func = [4, 6]

    #     sa = [
    #         { 'type': 'ge', 'idx': [3.0, 2.0], 'z': 24.0},
    #         { 'type': 'ge', 'idx': [2.0, 6.0], 'z': 30.0}
    #     ]

    #     result, z = simplex(func, sa)

    #     self.assertAlmostEqual(z, 42)

    #     expected = [6, 3]
        
    #     for i, x in enumerate(result):
    #         self.assertAlmostEqual(x, expected[i])

    # # @unittest.skip("")
    # def test_lista2(self):
    #     func = [-4, -5]

    #     sa = [
    #         { 'type': 'e', 'idx': [1.0, 1.0], 'z': 98.0},
    #         { 'type': 'ge', 'idx': [2.0, -1.0], 'z': 10.0},
    #         { 'type': 'le', 'idx': [-2.0, 1.0], 'z': 5.0}
    #     ]

    #     result, z = simplex(func, sa)

    #     self.assertAlmostEqual(z, -454)

    #     expected = [36, 62]
        
    #     for i, x in enumerate(result):
    #         self.assertAlmostEqual(x, expected[i])

    # # @unittest.skip("")
    # def test_lista4(self):
    #     func = [2, 2, 3]

    #     sa = [
    #         { 'type': 'ge', 'idx': [-1.0, 2.0, 5.0], 'z': 30.0},
    #         { 'type': 'ge', 'idx': [3.0, 4.0, -1.0], 'z': 60.0},
    #         { 'type': 'e', 'idx': [2.0, 1.0, 2.0], 'z': 40.0}
    #     ]

    #     result, z = simplex(func, sa)

    #     self.assertAlmostEqual(z, 53)

    #     expected = [11, 8, 5]
        
    #     for i, x in enumerate(result):
    #         self.assertAlmostEqual(x, expected[i])

    # # @unittest.skip("")
    # def test_lista5(self):
    #     func = [-10, -12]

    #     sa = [
    #         { 'type': 'le', 'idx': [1.0, 1.0], 'z': 100.0},
    #         { 'type': 'le', 'idx': [2.0, 3.0], 'z': 270.0}
    #     ]

    #     result, z = simplex(func, sa)

    #     self.assertAlmostEqual(z, -1140)

    #     expected = [30, 70]
        
    #     for i, x in enumerate(result):
    #         self.assertAlmostEqual(x, expected[i])

    # # @unittest.skip("")
    # def test_lista6(self):
    #     func = [-2, -3, -4]

    #     sa = [
    #         { 'type': 'le', 'idx': [1.0, 1.0, 1.0], 'z': 100.0},
    #         { 'type': 'le', 'idx': [2.0, 1.0, 0.0], 'z': 210.0},
    #         { 'type': 'le', 'idx': [1.0, 0.0, 0.0], 'z': 80.0}
    #     ]

    #     result, z = simplex(func, sa)

    #     self.assertAlmostEqual(z, -400)

    #     expected = [0, 0, 100]
        
    #     for i, x in enumerate(result):
    #         self.assertAlmostEqual(x, expected[i])

if __name__ == '__main__':
    unittest.main()
