resource "aws_iam_user" "users" {

count =5
name = "user-${count.index + 1}"
}

resource "aws_iam_group" "admin_group" {

name= "AdminGroup"
}

resource "aws_iam_group" "storage_group" {

name= "StorageGroup"
}


resource "aws_iam_policy" "admin_policy" {
name= "Admin-Policy"
description = "Policy for administrators"
policy = jsonencode({
Version = "2012-10-17"
Statement = [
{
Effect = "Allow"
Action = "*"
Resource = "*"
}
]
})
}

resource "aws_iam_policy" "storage_policy" {
name = "StoragePolicy"
description = "Policy for storage access"
policy = jsonencode({
Version = "2012-10-17"
Statement = [
{
Effect = "Allow"
Action = [
"s3:*"
]
"Resource" = "*"
}
]
})
}


resource "aws_iam_group_policy_attachment" "admin_group_attachment" {
group = aws_iam_group.admin_group.name
policy_arn = aws_iam_policy.admin_policy.arn
}


resource "aws_iam_group_policy_attachment" "storage_group_attachment" {
group = aws_iam_group.storage_group.name
policy_arn = aws_iam_policy.storage_policy.arn
}


variable "AdminUsers_to_attach" {
type = list(string)
default = ["user-1", "user-2", "user-3"]
}


resource "aws_iam_group_membership" "AdminGroup_membership" {
for_each = { for idx, user in var.AdminUsers_to_attach : idx => user }
name = "${each.value}-membership"
users = [each.value]
group = aws_iam_group.admin_group.name
}


variable "StorageUsers_to_attach" {
type = list(string)
default = ["user-4", "user-5"]
}


resource "aws_iam_group_membership" "StorageGroup_membership" {
for_each = { for idx, user in var.StorageUsers_to_attach : idx => user }
name = "${each.value}-membership"
users = [each.value]
group = aws_iam_group.storage_group.name
}

