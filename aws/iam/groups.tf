
resource "aws_iam_group" "admin_group" {

  name = "AdminGroup"
}

resource "aws_iam_group" "storage_group" {

  name = "StorageGroup"
}