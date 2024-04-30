variable "inst_type" {
    default = {
        "dev"  = "t2.micro",
        "qa"   = "t3.micro",
        "prod" = "t2.large"
    }
}

variable "region" {
    default = {
        "dev" = "us-east-1"
        "qa" = "us-west-1"
        "prod" = "eu-central-1"
    }
}