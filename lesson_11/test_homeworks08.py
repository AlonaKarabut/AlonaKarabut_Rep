import unittest
from unittest.mock import patch

"""_______sumStringNumbers_______"""

from homeworks import sumStringNumbers

class TestSumStringNumbers(unittest.TestCase):

    def setUp(self):
        print(f"\nПочаток тесту: {self._testMethodName}")

    def tearDown(self):
        print(f"Завершення тесту: {self._testMethodName}")

    def test_sumStringNumbers_IsNotNone(self):
        result = sumStringNumbers()
        self.assertIsNotNone(result, msg="Result must not be None")

    def test_sumStringNumbers_IsInstance_list(self):
        result = sumStringNumbers()
        self.assertIsInstance(result, list, msg="Result must be a list")

    def test_sumStringNumbers_ListEqual(self):
        result = sumStringNumbers()
        self.assertListEqual(result, [10, 60, 'Не можу це зробити!'], msg="Result must be a list with next data: [10, 60, 'Не можу це зробити!']")

"""_______sumOfAllEvenNumbers_______"""

from homeworks import sumOfAllEvenNumbers

class TestSumOfAllEvenNumbers(unittest.TestCase):

    def setUp(self):
        print(f"\nПочаток тесту: {self._testMethodName}")

    def tearDown(self):
        print(f"Завершення тесту: {self._testMethodName}")

    def test_sumOfAllEvenNumbers_IsInstance_int(self):
        result = sumOfAllEvenNumbers()
        self.assertIsInstance(result, int, msg="Result must be an int")

    def test_sumOfAllEvenNumbers_Equal(self):
        result = sumOfAllEvenNumbers()
        self.assertEqual(result, 110, msg="Result must be 110")

"""_______countUniqueSymbols_______"""

from homeworks import countUniqueSymbols

class TestCountUniqueSymbols(unittest.TestCase):

    def setUp(self):
        print(f"\nПочаток тесту: {self._testMethodName}")

    def tearDown(self):
        print(f"Завершення тесту: {self._testMethodName}")

    @patch('builtins.input', return_value='аbcd')
    def test_countUniqueSymbols_IsInstance_bool(self, mock_input):
        result = countUniqueSymbols()
        self.assertIsInstance(result, bool, msg="Result must be a bool")

    @patch('builtins.input', return_value='аbcd')
    def test_countUniqueSymbols_isFalse(self, mock_input):
        result = countUniqueSymbols()
        self.assertFalse(result, msg="Result must be False")

    @patch('builtins.input', return_value='аbcdefghijklmn')
    def test_countUniqueSymbols_IsInstance_bool(self, mock_input):
        result = countUniqueSymbols()
        self.assertIsInstance(result, bool, msg="Result must be a bool")

    @patch('builtins.input', return_value='аbcdefghijklmn')
    def test_countUniqueSymbols_isTrue(self, mock_input):
        result = countUniqueSymbols()
        self.assertTrue(result, msg="Result must be True")

"""_______enterWordWithH_______"""

from homeworks import enterWordWithH

class TestEnterWordWithH(unittest.TestCase):

    def setUp(self):
        print(f"\nПочаток тесту: {self._testMethodName}")

    def tearDown(self):
        print(f"Завершення тесту: {self._testMethodName}")

    @patch('builtins.input', return_value='light')
    def test_enterWordWithH_IsInstance_str(self, mock_input):
        result = enterWordWithH()
        self.assertIsInstance(result, str, msg="Result must be a string")

    @patch('builtins.input', return_value='light')
    def test_enterWordWithH_IsInstance_str(self, mock_input):
        result = enterWordWithH()
        self.assertEqual(result, "Thank you, good job!", msg="Result must be 'Thank you, good job!'.")

    @patch('builtins.input', return_value='darkness')
    def test_enterWordWithH_IsInstance_str(self, mock_input):
        result = enterWordWithH()
        self.assertIsInstance(result, str, msg="Result must be a string")

    @patch('builtins.input', return_value='darkness')
    def test_enterWordWithH_IsInstance_str(self, mock_input):
        result = enterWordWithH()
        self.assertEqual(result, "Sorry, you entered word containing no letter 'h'. Try again.", msg="Result must be \"Sorry, you entered word containing no letter 'h'. Try again.\"")

"""_______enterWordWithH_______"""

from homeworks import findLongestWord

class TestFindLongestWord(unittest.TestCase):

    def setUp(self):
        print(f"\nПочаток тесту: {self._testMethodName}")

    def tearDown(self):
        print(f"Завершення тесту: {self._testMethodName}")

    @patch('builtins.input', return_value='one twenty zero')
    def test_findLongestWord_IsInstance_str(self, mock_input):
        result = findLongestWord()
        self.assertIsInstance(result, str, msg="Result must be a string")

    @patch('builtins.input', return_value='one twenty zero')
    def test_findLongestWord_Equal(self, mock_input):
        result = findLongestWord()
        self.assertEqual(result, "twenty", msg="Result must be 'twenty'")



if __name__ == "__main__":
    unittest.main()
