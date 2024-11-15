import boto3
import json
import os

# Load environment variables for AWS credentials (if set)
aws_region = os.environ.get('AWS_REGION', 'us-east-1')
sqs_queue_name = os.environ.get('SQS_QUEUE_NAME', 'tf-task-sqs-queue')
s3_bucket_name = os.environ.get('S3_BUCKET_NAME', 'tf-task-bucket')
secret_name = os.environ.get('SECRET_NAME', 'tf-task-secret')
ec2_instance_id = os.environ.get('EC2_INSTANCE_ID', 'i-0c7cce62444d47623')

# Initializing AWS clients
sqs_client = boto3.client('sqs', region_name=aws_region)
s3_client = boto3.client('s3', region_name=aws_region)
secrets_manager_client = boto3.client('secretsmanager', region_name=aws_region)
ec2_client = boto3.client('ec2', region_name=aws_region)

# Get the URL of the SQS queue
def get_queue_url(queue_name):
    try:
        response = sqs_client.get_queue_url(QueueName=queue_name)
        return response['QueueUrl']
    except sqs_client.exceptions.QueueDoesNotExist:
        print(f"Queue {queue_name} does not exist.")
        return None

# Send a message to the SQS queue
def send_message_to_sqs(message_body):
    queue_url = get_queue_url(sqs_queue_name)
    if queue_url:
        response = sqs_client.send_message(
            QueueUrl=queue_url,
            MessageBody=message_body
        )
        print(f"Message sent to SQS Queue: {response['MessageId']}")

# Upload a file to S3
def upload_to_s3(file_name, data):
    try:
        response = s3_client.put_object(
            Bucket=s3_bucket_name,
            Key=file_name,
            Body=data
        )
        print(f"File uploaded to S3: {response['ETag']}")
    except Exception as e:
        print(f"Failed to upload file to S3: {e}")

# Retrieving a secret from Secrets Manager
def get_secret_from_secrets_manager(secret_name):
    try:
        response = secrets_manager_client.get_secret_value(SecretId=secret_name)
        secret = json.loads(response['SecretString'])
        print(f"Secret retrieved: {secret}")
        return secret
    except secrets_manager_client.exceptions.ResourceNotFoundException:
        print(f"Secret {secret_name} not found.")
        return None

# Describe the EC2 instance
def describe_ec2_instance(instance_id):
    try:
        response = ec2_client.describe_instances(InstanceIds=[instance_id])
        instance = response['Reservations'][0]['Instances'][0]
        print(f"EC2 Instance ID: {instance['InstanceId']}")
        print(f"EC2 Instance Type: {instance['InstanceType']}")
        print(f"EC2 Public IP: {instance.get('PublicIpAddress', 'No Public IP')}")
        print(f"EC2 State: {instance['State']['Name']}")
        print(f"EC2 Launch Time: {instance['LaunchTime']}")
    except Exception as e:
        print(f"Failed to describe EC2 instance: {e}")

if __name__ == "__main__":
    # Send a test message to SQS
    send_message_to_sqs("Hello, SQS! This is a test message.")
    
    # Upload a test file to S3
    upload_to_s3("testfile.txt", "This is a test file uploaded from the Python app.")

    # Retrieve a secret from Secrets Manager
    secret = get_secret_from_secrets_manager(secret_name)
    
    # Get EC2 instance information
    describe_ec2_instance(ec2_instance_id)
