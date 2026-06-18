import unittest

def number_greater_than_second(n):
    if len(n) < 2:
        return False
    
    second = n[1]
    result = []

    for i in n:
        if i > second:
            result.append(i)
    return result

class TestFun(unittest.TestCase):
    def testTwo(self):
        self.assertEqual(number_greater_than_second([1,2,3,1,5,]),False)
        
        
if __name__ == '__main__':
    unittest.main()
        
