import unittest

from parse import parse_restriction, parse_function

class ParseTest(unittest.TestCase):
    def test_type_equals(self):
        eq = parse_restriction('x1 = 3')
        self.assertEquals(eq['type'], 'e')

    def test_type_less_or_equal(self):
        eq = parse_restriction('x1 <= 3')
        self.assertEquals(eq['type'], 'le')

    def test_type_greather_or_equal(self):
        eq = parse_restriction('x1 >= 3')
        self.assertEquals(eq['type'], 'ge')

    def test_z_value(self):
        eq = parse_restriction('x1 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

    def test_x1_value(self):
        eq = parse_restriction('1x1 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

        self.assertAlmostEqual(len(eq['idx']), 1)
        self.assertAlmostEqual(eq['idx'][0], 1)

    def test_x1_x2_value(self):
        eq = parse_restriction('1x1 + 2x2 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

        self.assertAlmostEqual(len(eq['idx']), 2)
        self.assertAlmostEqual(eq['idx'][0], 1)
        self.assertAlmostEqual(eq['idx'][1], 2)

    def test_x1_neg_x2_value(self):
        eq = parse_restriction('-1x1 + 2x2 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

        self.assertAlmostEqual(len(eq['idx']), 2)
        self.assertAlmostEqual(eq['idx'][0], -1)
        self.assertAlmostEqual(eq['idx'][1], 2)

    def test_x1_x2_neg_value(self):
        eq = parse_restriction('1x1 - 2x2 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

        self.assertAlmostEqual(len(eq['idx']), 2)
        self.assertAlmostEqual(eq['idx'][0], 1)
        self.assertAlmostEqual(eq['idx'][1], -2)

    def test_x1_neg_x2_neg_value(self):
        eq = parse_restriction('- 1x1 - 2x2 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

        self.assertAlmostEqual(len(eq['idx']), 2)
        self.assertAlmostEqual(eq['idx'][0], -1)
        self.assertAlmostEqual(eq['idx'][1], -2)

    def test_x1_x2_x3_x4_value(self):
        eq = parse_restriction('1x1 + 2x2 - 4x3 + 5x4 = 3')
        self.assertEquals(eq['type'], 'e')
        self.assertAlmostEqual(eq['z'], 3)

        self.assertAlmostEqual(len(eq['idx']), 4)
        self.assertAlmostEqual(eq['idx'][0], 1)
        self.assertAlmostEqual(eq['idx'][1], 2)
        self.assertAlmostEqual(eq['idx'][2], -4)
        self.assertAlmostEqual(eq['idx'][3], 5)

    def test_function(self):
        function = parse_function('1x1+2x2')
        self.assertAlmostEqual(len(function), 2)
        self.assertAlmostEqual(function[0], 1)
        self.assertAlmostEqual(function[1], 2)

    def test_function_neg(self):
        function = parse_function('-1x1-2x2')
        self.assertAlmostEqual(len(function), 2)
        self.assertAlmostEqual(function[0], -1)
        self.assertAlmostEqual(function[1], -2)

if __name__ == '__main__':
    unittest.main()

