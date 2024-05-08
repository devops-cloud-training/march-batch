locals {
    profile = join("aws_profile=",terraform.workspace)
    instance = lookup(var.inst_type,terraform.workspace,"t2.micro")
}