import os, sys
modulePath = os.path.abspath("../PdfSplitter")
if modulePath not in sys.path:
    sys.path.insert(0, modulePath)


import unittest
from PdfSplitter import Splitter

class TestSplitter(unittest.TestCase):
    """docstring for TestSplitter."""
