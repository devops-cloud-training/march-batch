import boto3

from rich import print

iam_resource = boto3.resource("iam")

# policies = iam_resource.policies.all()

# print(policies)
# counter = 0

# for policy in policies:
#     counter += 1 #counter = counter + 1
# print(counter)

iam_client = boto3.client("iam")

# policies = iam_client.list_policies()
# print(len(policies["Policies"]))

#paginator

paginator = iam_client.get_paginator('list_policies')
pages = paginator.paginate()
counter = 0
no_of_policies = 0
# print(pages)
for i in pages:
    # print(i)
    counter += 1
    policies_in_one_page = i["Policies"]
    for policy in policies_in_one_page:
        no_of_policies += 1
        print(policy["Arn"])
print("No of pages",counter)
print("No of policies",no_of_policies)