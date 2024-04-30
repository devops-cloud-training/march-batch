resource "aws_s3_bucket" "example" {
  bucket = "sathish-new-bucket-1"

  tags = {
    Name        = "My bucket"
    Environment = "Dev"
  }
}


resource "aws_instance" "my_first_server" {
  ami                     = "ami-04e5276ebb8451442"
  instance_type           = "t2.micro"
}

resource "aws_iam_user" "users" {
  name  = "sathish123"
}


resource "aws_iam_user" "users" {
  name  = "sathish123e32434"
}
