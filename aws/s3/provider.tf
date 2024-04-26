terraform {
  required_providers {
    local = {
      source  = "hashicorp/local"
      version = "2.4.0"
    }
    aws = {
      source  = "hashicorp/aws"
      version = "5.25.0"
    }
  }
  backend "s3" {
    bucket = "sathish-class-bucket-1"
    key    = "terraform.tfstate"
    region = "us-east-1"
    dynamodb_table = "state-lock"
  }
}