provider "aws" {
    region = lookup(var.region,terraform.workspace,"us-east-1")
    profile = local.profile
}

# 