resource "aws_instance" "my_first_server" {
  ami                     = "ami-04e5276ebb8451442"
  instance_type           = lookup(var.inst_type,terraform.workspace,"t2.micro")
}
