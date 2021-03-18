import unittest
import blanagram_checker


class TestMethods(unittest.TestCase):
    
    def test_very_similar_strings(self):
        self.assertEqual(blanagram_checker.is_blanagram("ABC ", "AcB."), True)
    
    def test_similar_strings(self):
        self.assertEqual(blanagram_checker.is_blanagram("dABC", "AcB.g"), True)


if __name__ == '__main__':
    unittest.main()