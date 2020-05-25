# test-aws-lambda-pipeline

prerequisites:\
installed: _python3_ and _pip3_
 
steps:\
install venv:\
`$ source venv/bin/activate`\

install dependencies:\
`$ pip3 install -r requirements.txt`\

set-up aws credentials:\
`$ aws configure`

You will be given the next questions:
>Your AWS Access Key\
Your AWS Secret Access Key\
A “Default region name” – enter us-east-1\
A “Default output format” – enter json

to run tests:
`$ pytest run`

to run tests and get allure reporting:
`$ pytest --alluredir=allure_results`
`$ pallure serve allure_results/`


All founded bugs were tracked and put into bug_reports file
