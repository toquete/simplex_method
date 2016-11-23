import unittest

from parse import parse

class ParseTest(unittest.TestCase):
    #{ 'type': 'le', 'idx': [1.0, 1.0, 1.0], 'z': 100.0},
    def test_type_equals(self):
        eq = parse('x1 = 3')
        self.assertEquals(eq['type'], 'e')

    def test_type_less_or_equal(self):
        eq = parse('x1 <= 3')
        self.assertEquals(eq['type'], 'le')

    def test_type_greather_or_equal(self):
        eq = parse('x1 >= 3')
        self.assertEquals(eq['type'], 'ge')

    def test_z_value(self):
        eq = parse('x1 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

    def test_x1_value(self):
        eq = parse('1x1 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

        self.assertAlmostEqual(len(eq['idx']), 1)
        self.assertAlmostEqual(eq['idx'][0], 1)

    def test_x1_x2_value(self):
        eq = parse('1x1 + 2x2 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

        self.assertAlmostEqual(len(eq['idx']), 2)
        self.assertAlmostEqual(eq['idx'][0], 1)
        self.assertAlmostEqual(eq['idx'][1], 2)

    def test_x1_neg_x2_value(self):
        eq = parse('-1x1 + 2x2 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

        self.assertAlmostEqual(len(eq['idx']), 2)
        self.assertAlmostEqual(eq['idx'][0], -1)
        self.assertAlmostEqual(eq['idx'][1], 2)

    def test_x1_x2_neg_value(self):
        eq = parse('1x1 - 2x2 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

        self.assertAlmostEqual(len(eq['idx']), 2)
        self.assertAlmostEqual(eq['idx'][0], 1)
        self.assertAlmostEqual(eq['idx'][1], -2)

    def test_x1_neg_x2_neg_value(self):
        eq = parse('- 1x1 - 2x2 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

        self.assertAlmostEqual(len(eq['idx']), 2)
        self.assertAlmostEqual(eq['idx'][0], -1)
        self.assertAlmostEqual(eq['idx'][1], -2)

if __name__ == '__main__':
    unittest.main()

