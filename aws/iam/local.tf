locals {
  merged_user_list = distinct(concat(var.storage_user_ids, var.admin_user_ids))

  #merged_user_list = tolist(setunion(var.storage_user_ids, var.admin_user_ids))

}