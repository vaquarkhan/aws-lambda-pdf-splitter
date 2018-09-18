import os, sys
modulePath = os.path.abspath("../PdfSplitter")
if modulePath not in sys.path:
    sys.path.insert(0, modulePath)


from ConfigEnv import Config
import unittest
import boto3

from PdfSplitter import Splitter

class TestSplitter(unittest.TestCase):
    """docstring for TestSplitter."""

    def setUp(self):
        self._config = Config(self.getCurrentPath()+"data/testConfig.json")
        self._config.addFile = Config(self.getCurrentPath()+"data/splitterConfig.json")
        s3 = boto3.resource(
            's3',
            'eu-west-1',
            aws_access_key_id=self._config.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=self._config.get("AWS_SECRET_ACCESS_KEY"),
            aws_session_token= self._config.get("AWS_SESSION_TOKEN")
        )

        self._letterKey = self.getCurrentPath()+"data/pdf/letter.pdf";
        self._numberKey = self.getCurrentPath()+"data/pdf/number.pdf";

        bucket = s3.Bucket(self._config.get("AWS_S3_BUCKET"))

        # uplaod sur le bucket de données de test
        bucket.upload_file(self._letterKey, 'letter.pdf')
        bucket.upload_file(self._numberKey, 'number.pdf')

    def getCurrentPath(self):
        return os.path.dirname(os.path.abspath(__file__))+"/"

    def test__init__(self):
        splitter = Splitter(self.getCurrentPath()+"data/splitterConfig.json")
        for object in splitter._s3.Bucket(self._config.get("AWS_S3_BUCKET")).objects.all():
            print( object )
