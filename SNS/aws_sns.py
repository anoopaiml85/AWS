import boto3
import os
client = boto3.client('sns',aws_access_key_id= os.environ.get('AWS_ACCESS_KEY_ID'),aws_secret_access_key= os.environ.get('AWS_SECRET_ACCESS_KEY'),region_name= os.environ.get('REGION_NAME'))
email_body = '<h1>Hello &nbsp from SNS</h1>'
client.publish(TargetArn='arn:aws:sns:us-east-2:743219909737:Anoop_test',
            Message=email_body, Subject='Hello', MessageStructure='string',
             )
                  