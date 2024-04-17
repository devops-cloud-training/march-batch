# How to use variables
# you can mention it in default value of variable

# variables can be prompted in CLI while running your terraform code (it will prompt while running tf plan & apply)
# var.firstfile_filename
#  This provides a filename for the first file getting created

#  Enter a value:

# provide terraform variables via CLI while running code 
#  terraform plan -var="firstfile_filename=abc.txt"

# Providing variables via environment variable
# export TF_VAR_firstfile_filename=xyz.txt

# Providing variables values via tfvars file 
# terraform plan -var-file=values.tfvars



variable "firstfile_filename" {
  description = "This provides a filename for the first file getting created"
  type        = string
  default     = "default_file.txt"
}

variable "firstfile_content" {
  default     = "Hey! Welcome to the first terraform execution! all the best!"
  description = "This provides a content for the first file getting created"
  type        = string
}

variable "countfile_name" {
  type = set(string)
  default = [
    "india.txt",
    "america.txt",
    "portugal.txt",
    "pakistan.txt",
    "uk.txt",
    "france.txt",
    "mexico.txt",
    "canada.txt",
    "india.txt",
    "canada.txt",
    "portugal.txt"
  ]
}