#Assignment1 -- 5 users and 2 groups (u1,u2,u3-> admingroup),(u4,u5 -> storagegroup), admingroup-fulladministratoraccess,storagegroup- fulls3acess


resource "aws_iam_user" "u1" {
name = "user1"
}
resource "aws_iam_user" "u2" {
name = "user2"
}
resource "aws_iam_user" "u3" {
name = "user3"
}
resource "aws_iam_user" "u4" {
name = "user4"
}
resource "aws_iam_user" "u5" {
name = "user5"
}

resource "aws_iam_group" "admin" {
name = "administrator"
}

resource "aws_iam_group" "storageadmin" {
name = "storage_administrator"
}

resource "aws_iam_group_policy" "admin_policy" {
name = "administrator_policy"
group = aws_iam_group.admin.name
policy = jsonencode({
Version = "2012-10-17"
Statement = [
{
Action = "*"
Effect = "Allow"
Resource = "*"
},
]
})
}

resource "aws_iam_group_policy" "storageadmin_policy" {
name = "storage_administrator_policy"
group = aws_iam_group.storageadmin.name
policy = jsonencode({
Version = "2012-10-17"
Statement = [
{
Action = "s3:*"
Effect = "Allow"
Resource = "*"
},
]
})
}

resource "aws_iam_group_membership" "adminteam" {
name = "admin-group-membership"

users = [
aws_iam_user.u1.name,
aws_iam_user.u2.name,
aws_iam_user.u3.name,
]

group = aws_iam_group.admin.name
}

resource "aws_iam_group_membership" "storageadminteam" {
name = "storageadmin-group-membership"

users = [
aws_iam_user.u4.name,
aws_iam_user.u5.name,
]

group = aws_iam_group.storageadmin.name
}

