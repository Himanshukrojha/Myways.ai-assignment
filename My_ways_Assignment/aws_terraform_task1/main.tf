provider "aws" {
  region = var.aws_region
}
resource "aws_s3_bucket" "my_bucket" {
  bucket = var.s3_bucket_name
  acl    = "private"
}
resource "aws_sqs_queue" "my_queue" {
  name = var.queue_name
}
resource "aws_secretsmanager_secret" "my_secret" {
  name        = var.secret_name
  description = "Secret for my application"
}

resource "aws_secretsmanager_secret_version" "my_secret_version" {
  secret_id     = aws_secretsmanager_secret.my_secret.id
  secret_string = jsonencode({
    username = "Himanshu",
    password = "Himanshu123"
  })
}
resource "aws_instance" "my_instance" {
  ami           = "ami-073e3b46f8802d31b"
  instance_type = var.instance_type
  tags = {
    Name = "MyAppInstance"
  }
}

