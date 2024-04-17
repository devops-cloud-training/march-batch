variable "storage_user_ids" {
  description = "The list of user ids for storage group"
  type        = list(string)
}

variable "admin_user_ids" {
  description = "The list of user ids for admin group"
  type        = list(string)
}