from argparse import Namespace
from datetime import date
from pathlib import Path
import json
import os
import sys
import unittest
import time
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)),
                             os.path.pardir))
from cvs import Init, Add, Commit, Reset, Log, Checkout, System  # noqa


class TestCVS(unittest.TestCase):
    def setUp(self) -> None:
        pass

    def tearDown(self) -> None:
        pass


if __name__ == '__main__':
    unittest.main()
