variable "aws_region" {
  description = "AWS Region to deploy resources"
  default     = "us-east-1"
}

variable "instance_type" {
  description = "EC2 instance type"
  default     = "t2.micro"
}

variable "s3_bucket_name" {
  description = "terraform-task-s3bucket"
  default     = "tf-task-bucket"
}

variable "secret_name" {
  description = "Name of the secret in AWS Secrets Manager"
  default     = "tf-task-secret"
}

variable "queue_name" {
  description = "Name of the SQS queue"
  default     = "tf-task-sqs-queue"
}
