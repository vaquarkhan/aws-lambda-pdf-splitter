from PdfSplitter import Splitter


def lambdaPdfSplitter(event, context=None):
    spliter = Splitter()
    spliter.split(event)
    return true
