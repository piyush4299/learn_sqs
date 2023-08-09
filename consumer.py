from dotenv import load_dotenv
import boto3
import os

load_dotenv()

aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv('aws_secret_access_key')
queue_url = os.getenv('queue_url')

client = boto3.client('sqs', region_name='ap-southeast-2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

while True:
    response = client.receive_message(QueueUrl=queue_url, MaxNumberOfMessages=1)
    if 'Messages' in response:
        message = response['Messages'][0]
        receipt_handle = message['ReceiptHandle']
        body = message['Body']
        
        print(f'Received message: {body}')
        # Delete the message from the queue
        client.delete_message(QueueUrl=queue_url, ReceiptHandle=receipt_handle)
    else:
        print('No messages in queue')
        break