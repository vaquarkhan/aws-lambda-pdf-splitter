from ConfigEnv import Config
from PyPDF2 import PdfFileWriter, PdfFileReader
import boto3

class Splitter():
    """docstring for Splitter."""

    def __init__(self, configFile = None):
        self._config = Config(configFile)
        self._cachePage = {}
        self._s3 = boto3.resource(
            's3',
            'eu-west-1',
            aws_access_key_id=self._config.get("AWS_ACCESS_KEY_ID"),
            aws_secret_access_key=self._config.get("AWS_SECRET_ACCESS_KEY"),
            aws_session_token= self._config.get("AWS_SESSION_TOKEN")
        )
