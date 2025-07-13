import pytest
from unittest.mock import patch

"""_______sumStringNumbers_______"""

from homeworks import sumStringNumbers

def test_sumStringNumbers_IsNotNone():
    result = sumStringNumbers()
    assert result is not None

def test_sumStringNumbers_IsInstance_list():
    result = sumStringNumbers()
    assert isinstance(result, list)

def test_sumStringNumbers_ListEqual():
    result = sumStringNumbers()
    assert result == [10, 60, 'Не можу це зробити!']

"""_______sumOfAllEvenNumbers_______"""

from homeworks import sumOfAllEvenNumbers

def test_sumOfAllEvenNumbers_IsInstance_int():
    result = sumOfAllEvenNumbers()
    assert isinstance(result, int)

def test_sumOfAllEvenNumbers_Equal():
    result = sumOfAllEvenNumbers()
    assert result == 110

"""_______countUniqueSymbols_______"""

from homeworks import countUniqueSymbols

@patch('builtins.input', return_value='аbcd')
def test_countUniqueSymbols_IsInstance_bool(mock_input):
    result = countUniqueSymbols()
    assert isinstance(result, bool)

@patch('builtins.input', return_value='аbcd')
def test_countUniqueSymbols_isFalse(mock_input):
    result = countUniqueSymbols()
    assert result is False

@patch('builtins.input', return_value='аbcdefghijklmn')
def test_countUniqueSymbols_IsInstance_bool(mock_input):
    result = countUniqueSymbols()
    assert isinstance(result, bool)

@patch('builtins.input', return_value='аbcdefghijklmn')
def test_countUniqueSymbols_isTrue(mock_input):
    result = countUniqueSymbols()
    assert result is True

"""_______enterWordWithH_______"""

from homeworks import enterWordWithH

@patch('builtins.input', return_value='light')
def test_enterWordWithH_IsInstance_str(mock_input):
    result = enterWordWithH()
    assert isinstance(result, str)

@patch('builtins.input', return_value='light')
def test_enterWordWithH_IsInstance_str(mock_input):
    result = enterWordWithH()
    assert result == "Thank you, good job!"

@patch('builtins.input', return_value='darkness')
def test_enterWordWithH_IsInstance_str(mock_input):
    result = enterWordWithH()
    assert isinstance(result, str)

@patch('builtins.input', return_value='darkness')
def test_enterWordWithH_IsInstance_str(mock_input):
    result = enterWordWithH()
    assert result == "Sorry, you entered word containing no letter 'h'. Try again."



"""_______enterWordWithH_______"""

from homeworks import findLongestWord

@patch('builtins.input', return_value='one twenty zero')
def test_findLongestWord_IsInstance_str(mock_input):
    result = findLongestWord()
    assert isinstance(result, str)

@patch('builtins.input', return_value='one twenty zero')
def test_findLongestWord_Equal(mock_input):
    result = findLongestWord()
    assert result == "twenty"