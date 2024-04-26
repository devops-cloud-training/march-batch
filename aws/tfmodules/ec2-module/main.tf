resource "aws_instance" "server" {
    ami = var.ami_id_provided ? var.ami_id : "ami-04e5276ebb8451442"
    instance_type = var.inst_type
}