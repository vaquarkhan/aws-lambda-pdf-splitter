import os, sys
modulePath = os.path.abspath("../PdfSplitter")
if modulePath not in sys.path:
    sys.path.insert(0, modulePath)


from ConfigEnv import Config
import unittest


from PdfSplitter import Splitter

class TestSplitter(unittest.TestCase):
    """docstring for TestSplitter."""

    def setUp(self):
        self._config = Config(self.getCurrentPath()+"data/testConfig.json")

    def getCurrentPath(self):
        return os.path.dirname(os.path.abspath(__file__))+"/"

    def test__init__(self):
        splitter = Splitter(self.getCurrentPath()+"data/splitterConfig.json")
        for object in splitter._s3.Bucket(self._config.get("AWS_S3_BUCKET")).objects.all():
            print( object )
