# test-aws-lambda-pipeline

prerequisites:\
installed: _python3_ and _pip3_
 
steps:\
install venv\
`$ source venv/bin/activate`\
`$ pip3 install -r requirements.txt`\
`$ aws configure`

You will be given the next questions:
>Your AWS Access Key\
Your AWS Secret Access Key\
A “Default region name” – enter us-east-1\
A “Default output format” – enter json

`$ pytest run`
