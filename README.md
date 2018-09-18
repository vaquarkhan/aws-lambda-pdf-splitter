# aws-lambda-pdf-splitter
Python pdf spliter hosted on AWS Lambda


## Developpement guide

### installation

with virtualenv :

    # create virtualenv
    virtualenv -p python3 .venv

    # activate venv
    source .venv/bin/activate

    # install dependancies
    pip install -r requirements.txt

### testing

with unittest :

    # if your test config is setup :
    python -m unittest

    # if you want to overide your test config : 
    AWS_S3_BUCKET=<your bucket> AWS_ACCESS_KEY_ID=<your key id> AWS_SECRET_ACCESS_KEY=<your key secret> python -m unittest
