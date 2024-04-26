module "myserver" {
    source = "github.com/terraform-aws-modules/terraform-aws-ec2-instance"

    ami = "ami-04e5276ebb8451442"
    instance_type = "t2.micro"
}