# aws-lambda-pdf-splitter
Python pdf spliter hosted on AWS Lambda

## Lambda Configuration

Environment variables :

    AWS_S3_BUCKET : your bucket

python version :

    python3.6

handler :

    lambda.lambdaPdfSplitter

memory :

    1024mb

timeout :

    5min

role:

    basic lmabda execution role + s3 read and write
