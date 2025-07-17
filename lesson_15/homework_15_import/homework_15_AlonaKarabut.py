# 20 імпортів
# Імпорт ваших функцій, вбудованих, інстальованих (вже інстальовані знайдете в папці vevn -> libs)
# Застосовути всі види імпорту
# from ... import...
# import ....
# from ... import *
# from ... import ... as ....

from datetime import datetime
import pytz
utc = pytz.UTC
now = datetime.now(utc)
print(now)


from packaging import version
print(version.parse("1.0") < version.parse("2.0"))


import pip
print(pip.__version__)


import math
print(math.factorial(5))


from pathlib import Path
import csv
file_path = Path("data.csv")
print(file_path.name)


import logging
logging.basicConfig(level=logging.INFO)
logging.info("This is INFO logging")


import os
print(os.getcwd())


import unittest
from unittest.mock import patch


from colorama import Fore, Style
print(Fore.GREEN + 'Зелений текст' + Style.RESET_ALL)

from abc import ABC, abstractmethod


from homeworks import sumStringNumbers as ssn
print(ssn())


from homeworks import sumOfAllEvenNumbers as saen
print(saen())


from homeworks import enterWordWithH
print(enterWordWithH())

from homeworks import findLongestWord
print(findLongestWord())

from factorial import factorial
print(factorial(3))

from factorial import factor
print(factor(4))

from factorial import fact
print(fact(5))


from myExamples import *