#!/bin/bash

[ -e lambda.zip ] && rm lambda.zip

[ -d .temp ] && rm -rf .temp

mkdir .temp ;

cd .temp ;

cp -r ../PdfSplitter .;
cp -r ../lambda.py .;

virtualenv -p python3.6 .venv ;

source .venv/bin/activate ;

pip install -r ../requirements.txt ;

mv .venv/lib/python3.6/site-packages/* . ;

rm .venv -rf ;

chmod 755 -R .

zip -r9 ../lambda.zip * ;

cd .. ;

deactivate

rm -rf .temp ;

# aws lambda update-function-code --function-name pdf-splitter --zip-file fileb://lambda.zip
