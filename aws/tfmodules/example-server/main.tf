module "myserver" {
    source = "./../ec2-module"

    ami_id_provided = true
    ami_id = "ami-abc234234"
    inst_type = "t2.micro"
}