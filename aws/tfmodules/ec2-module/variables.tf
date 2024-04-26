variable "ami_id" {
    type = string
    description = "Provide AMI ID to create instance"
}

variable "inst_type" {
    type = string
    description = "Provide type of the instance"
}

variable "ami_id_provided" {
    default = false
}