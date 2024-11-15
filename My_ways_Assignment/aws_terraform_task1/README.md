# AWS Infrastructure Deployment with Terraform and Python Application

## Overview

This project demonstrates how to deploy AWS infrastructure using **Terraform** and interact with deployed AWS services via a **Python application**. The deployed services include **SQS**, **S3**, **Secrets Manager**, and an **EC2 instance**. The Python app interacts with these services to perform tasks like sending/receiving messages, uploading files, retrieving secrets, and checking EC2 instance status.

---

## Prerequisites

1. **AWS Account**: Make sure you have an AWS account.
2. **Terraform**: Install Terraform from [here](https://www.terraform.io/downloads).
3. **AWS CLI**: Install AWS CLI from [here](https://aws.amazon.com/cli/).
4. **Python**: Install Python 3.x. (Ensure `pip` is also installed).
5. **boto3**: Install the AWS SDK for Python using `pip install boto3`.

---

## Getting Started

### Step 1: Clone the Repository

```bash
git clone <repository_url>
cd aws_infrastructure_task
Step 2: Configure AWS CLI
Configure the AWS CLI with your credentials:

bash
Copy code
aws configure
Provide:

AWS Access Key ID
AWS Secret Access Key
Default region name (e.g., us-east-1)
Default output format (e.g., json)
Step 3: Define Variables in variables.tf
The variables.tf file defines AWS configurations like region, instance type, and resource names:

hcl
Copy code
variable "aws_region" {
  description = "AWS Region"
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "s3_bucket_name" {
  description = "S3 bucket name"
  default     = "tf-task-bucket"
}

variable "secret_name" {
  description = "Secret name in Secrets Manager"
  default     = "tf-task-secret"
}

variable "queue_name" {
  description = "SQS Queue name"
  default     = "tf-task-sqs-queue"
}
Step 4: Initialize Terraform
Initialize Terraform in your project directory to download the necessary provider plugins:

bash
Copy code
terraform init
Step 5: Apply Terraform Configuration
Apply the Terraform configuration to create the resources:

bash
Copy code
terraform apply
When prompted, type yes to confirm.

This will create:

SQS Queue for sending and receiving messages.
S3 Bucket for file storage.
Secrets Manager secret for sensitive data.
EC2 Instance to optionally host or interact with the application.
After completion, Terraform will output important resource information (e.g., Queue URL, S3 Bucket Name, EC2 Instance ID).

Step 6: Set Up the Python Application
The Python application (app.py) interacts with the AWS services. The script performs actions like sending messages to SQS, uploading files to S3, retrieving secrets, and managing the EC2 instance.

Environment Variables
Configure environment variables in the shell or set them directly in app.py:

bash
Copy code
export AWS_REGION=us-east-1
export SQS_QUEUE_NAME=tf-task-sqs-queue
export S3_BUCKET_NAME=tf-task-bucket
export SECRET_NAME=tf-task-secret
export EC2_INSTANCE_ID=<Your-EC2-Instance-ID>
Install Required Libraries
Use pip to install the necessary packages for Python:

bash
Copy code
pip install boto3
Run the Application
Execute the Python script to interact with the AWS services:

bash
Copy code
python app.py
The application will:

Send a message to the SQS queue.
Upload a test file to the S3 bucket.
Retrieve a secret from Secrets Manager.
Optionally interact with the specified EC2 instance.
Infrastructure Management
View Infrastructure State
To see the current state of your infrastructure, use:

bash
Copy code
terraform show
Update Infrastructure
Modify the Terraform configuration files as needed, then run:

bash
Copy code
terraform apply
Destroy Infrastructure
To clean up and remove all created resources:

bash
Copy code
terraform destroy
Confirm with yes to proceed.

Additional Resources
Terraform Documentation
boto3 Documentation
AWS CLI Documentation
```
