import boto3

client = boto3.client('sns',
                       aws_access_key_id='AKIA22C232RU3D2BTU7N',
                       aws_secret_access_key ='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',
                       region_name='us-east-2')
email_body = '<h1>Hello &nbsp from SNS</h1>'
client.publish(TargetArn='arn:aws:sns:us-east-2:743219909737:Anoop_test',
            Message=email_body, Subject='Hello', MessageStructure='string',
             )
                  