
resource "aws_iam_policy" "admin_policy" {
  name        = "Admin-Policy"
  description = "Policy for administrators"
  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [
      {
        Effect   = "Allow"
        Action   = "*"
        Resource = "*"
      }
    ]
  })
}

resource "aws_iam_policy" "storage_policy" {
  name        = "StoragePolicy"
  description = "Policy for storage access"
  policy = <<EOF
{
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
}
EOF
}
