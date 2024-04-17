resource "aws_iam_user" "users" {
  count = length(local.merged_user_list)
  name  = local.merged_user_list[count.index]
}
