import boto3
import json
import sys
import time
import os
import configparser
# config=configparser.ConfigParser()
# config.read("config.ini")
# from dotenv import load_dotenv
from os import environ as config
# load_dotenv()

#sqs = boto3.resource('sqs',aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY'),region_name=os.getenv('REGION_NAME'))
#sqs = boto3.resource('sqs',aws_access_key_id= os.environ.get('AWS_ACCESS_KEY_ID'),aws_secret_access_key= os.environ.get('AWS_SECRET_ACCESS_KEY'),region_name= os.environ.get('REGION_NAME'))
#sqs = boto3.resource('sqs',aws_access_key_id= config['AWS_ACCESS_KEY_ID'],aws_secret_access_key= config['credentials']['AWS_SECRET_ACCESS_KEY'],region_name= config['credentials']['REGION_NAME'])
sqs = boto3.resource('sqs',aws_access_key_id= config['AWS_ACCESS_KEY_ID'],aws_secret_access_key= config['AWS_SECRET_ACCESS_KEY'],region_name= config['REGION_NAME'])

#sqs=boto3.resource('sqs')

def create_queue(name,atr={}):
    queue=sqs.create_queue(QueueName=name,Attributes=atr)
    print(f"created queue with the name {name} with URL {queue.url}")

    #print(json.dumps(queue))


#create_queue('sqs_test2')    
def get_queue(name):
    queue=sqs.get_queue_by_name(QueueName=name)
    print(f"Got queue with the name {name} with URL {queue.url}")
    return queue

def get_queues(search=None):
    if search:
        queues=sqs.queues.filter(QueueNamePrefix=search)
    else:
        queues=sqs.queues.all()
    if queues:
        
       que= [q.url for q in queues]
       print(', '.join(que))
    else:
        print('No queue found.')   
    return que

def del_queue(name):
    
    queue=get_queue(name)
    delete_queue= queue.delete()
    print(f"queue deleted {delete_queue}")

    print(f"Deleted queue with the name {name} ; URL {queue.url}")
 

queue_name=sys.argv[1]
create_queue(queue_name)
get_queue(queue_name)
get_queues()
del_queue(queue_name)  
time.sleep(10)     
get_queues()

