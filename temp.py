


def getCorrectRange(first, second,step):
    if first > second:
        return list(range(first, second - 1, -step))
    return list(range(first, second + 1,step)) 


def getRangePoints(part, delimiter):
    first, second = part.split(delimiter)
    step = 1
    if ':' in second:
        second, step = second.split(':')
        if not step.strip().isnumeric():
            raise Exception('non numeric step value entered')
        step = int(step)

    if not first.strip().isnumeric() or not second.strip().isnumeric():
        raise Exception('non numeric value entered')
    return int(first), int(second), step

def rangeResolver(part,customDelimeters):
    part = part.strip()
    for delimiter in customDelimeters:
        if delimiter in part:
            first, second,step = getRangePoints(part, delimiter)
            return getCorrectRange(first, second,step)

    return [int(part)] if part.isnumeric() else []

    
    
def expander(s,customDelimeters=['-'],format = 'list',outputMode='as-it-is'):
    result = []
    s = s.strip()
    parts = s.split(',')
    for part in parts:
        if(part != ''):
            result.extend(rangeResolver(part,customDelimeters))
    
    if outputMode == 'sorted-unique':
        result = sorted(set(result))
    elif outputMode == 'unique':
        result = list(dict.fromkeys(result))
        
    if format == 'csv':
        return ','.join(map(str,result))
    elif format == 'set':
        return set(result)
    return result

print(expander('1-2,5-3,10~20:4',['-','~'],'list','unique'))
import unittest
import unittest

class TestRangeExpander(unittest.TestCase):

    def test_mix_ranges(self):
        input_str = "3-1,1-3,5 ,7~9,  ,   "
        expected = [3, 2, 1, 1, 2, 3, 5, 7, 8, 9]
        self.assertEqual(expander(input_str, ['-', '~']), expected)

    def test_step_value(self):
        self.assertEqual(expander("1~10:2", ['~']), [1, 3, 5, 7, 9])


    def test_sorted_unique(self):
        self.assertEqual(
            expander("3-1,1-3,5 ,7~9", ['-', '~'], outputMode='sorted-unique'),
            [1, 2, 3, 5, 7, 8, 9]
        )

    def test_unique_preserve_order(self):
        self.assertEqual(
            expander("3-1,1-3,5 ,7~9", ['-', '~'], outputMode='unique'),
            [3, 2, 1, 5, 7, 8, 9]
        )

    def test_csv_format(self):
        self.assertEqual(
            expander("1-3,2-2", ['-'], format='csv', outputMode='sorted-unique'),
            "1,2,3"
        )

    def test_set_format(self):
        result = expander("1-3,2-2", ['-'], format='set', outputMode='sorted-unique')
        self.assertEqual(result, {1, 2, 3})

if __name__ == "__main__":
    unittest.main()
