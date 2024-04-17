
resource "aws_iam_group_policy_attachment" "admin_group_attachment" {
  group      = aws_iam_group.admin_group.name
  policy_arn = aws_iam_policy.admin_policy.arn
}


resource "aws_iam_group_policy_attachment" "storage_group_attachment" {
  group      = aws_iam_group.storage_group.name
  policy_arn = aws_iam_policy.storage_policy.arn
}

resource "aws_iam_group_membership" "AdminGroup_membership" {
  name  = "admin_group"
  users = var.admin_user_ids
  group = aws_iam_group.admin_group.name
}

resource "aws_iam_group_membership" "StorageGroup_membership" {
  name  = "storage_group"
  users = var.storage_user_ids
  group = aws_iam_group.storage_group.name
}

