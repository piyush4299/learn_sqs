from dotenv import load_dotenv
import boto3
import os

load_dotenv()

aws_access_key_id = os.getenv("aws_access_key_id")
aws_secret_access_key = os.getenv('aws_secret_access_key')
queue_url = os.getenv('queue_url')

client = boto3.client('sqs', region_name='ap-southeast-2', aws_access_key_id=aws_access_key_id, aws_secret_access_key=aws_secret_access_key)

for numberOfMsg in range(5):
    message_body = 'hello world msgCnt=' + str(numberOfMsg)
    response = client.send_message(QueueUrl=queue_url, MessageBody=message_body)
    print('message sent: ' + str(numberOfMsg))
    print(f'Sent message: {response["MessageId"]}')
