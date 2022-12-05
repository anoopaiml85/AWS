import boto3

import os

client = boto3.clientboto3.client('sqs',aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),region_name=os.getenv('REGION_NAME'))
email_body = '<h1>Hello &nbsp from SNS</h1>'
client.publish(TargetArn='arn:aws:sns:us-east-2:743219909737:Anoop_test',
            Message=email_body, Subject='Hello', MessageStructure='string',
             )
                  
