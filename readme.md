# Handling passwords and secret keys 

Method 1: 

1 -- Using .env file

-->Create a .env file in the root of the project.
-->In the file profile the user name and the passwords or access keys. 
AWS_ACCESS_KEY_ID='xxxxxxxxxxxxxxxxxxxxxx' 
AWS_SECRET_ACCESS_KEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' 
REGION_NAME='us-east-2'

--> In the code import os and dotenv libraries
--> Load dotenv library load_dotenv().
--> access the env variables using os.getenv('AWS_ACCESS_KEY_ID')

Method 2:

2 -- Storing as global environment variables

--> Create a env.sh file in the root of the project.
--> in the file prvide the username and password or access keys. 
export AWS_ACCESS_KEY_ID='xxxxxxxxxxxxxxxxxxxxxx' 
export AWS_SECRET_ACCESS_KEY='xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' 
export REGION_NAME='us-east-2'

--> In the code import os 
--> access the env variables using 
os.environ.get('AWS_ACCESS_KEY_ID')

run the .py file from the terminal . ./env.sh && python ./SQS/sqs_queue.py sh_test2

