


def getCorrectRange(first: int, second: int) -> list:
    if first > second:
        return list(range(first, second - 1, -1))
    return list(range(first, second + 1)) 


def getRangePoints(part: str, delimiter: str):
    first, second = part.split(delimiter)
    if not first.strip().isnumeric() or not second.strip().isnumeric():
        raise Exception('non numeric value entered')
    return int(first), int(second)

def rangeResolver(part,customDelimeters):
    part = part.strip()
    for delimiter in customDelimeters:
        if delimiter in part:
            first, second = getRangePoints(part, delimiter)
            return getCorrectRange(first, second)

    return [int(part)] if part.isnumeric() else []

    
    
def expander(s,customDelimeters):
    result = []
    s = s.strip()
    parts = s.split(',')
    for part in parts:
        if(part != ''):
            result.extend(rangeResolver(part,customDelimeters))
    return result

import unittest

class TestRangeExpander(unittest.TestCase):

    def test_basic(self):
        self.assertEqual(rangeResolver("1-3", ['-']), [1, 2, 3])

    def test_changeDelimeterTest(self):
        self.assertEqual(rangeResolver("5~7", ['~']), [5, 6, 7])

    def test_reverseRangeTest(self):
        self.assertEqual(rangeResolver("5-2", ['-']), [5, 4, 3, 2])

    def test_nonNumericTest(self):
        with self.assertRaises(Exception) as context:
            rangeResolver("a-c", ['-', '~'])
        self.assertIn("non numeric value entered", str(context.exception))

    def test_mixTest(self):
        input_str = "3-1,1-3,5 ,7~9,  ,   "
        expected = [3, 2, 1, 1, 2, 3, 5, 7, 8, 9]
        self.assertEqual(expander(input_str, ['-', '~']), expected)

if __name__ == "__main__":
    unittest.main()
