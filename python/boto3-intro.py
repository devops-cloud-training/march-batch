import boto3
from rich import print
session = boto3.Session(region_name="us-east-2")

# print(dir(session))

# print(session.get_available_regions(service_name="ec2"))
# iam_resource = session.resource("iam")
# iam_client = session.client("iam")

# print(dir(iam_resource.users.all()))

# all_users = iam_resource.users.all()

# for i in all_users:
#     print(i.name)

# print(iam_client.list_users())

ec2_resource = session.resource("ec2")
ec2_client = session.client("ec2")

# instances_list = ec2_resource.instances.filter( Filters = [
#     {
#         "Name" : "instance-state-name",
#         "Values": ["running"]
#     }
# ] )

# for i in instances_list:
#     print(i.id)

# instance_id = []

# instances_list = ec2_resource.instances.filter( Filters = [
#     {
#         "Name" : "instance-state-name",
#         "Values": ["stopped"]
#     }
# ] )
# for i in instances_list:
#     print(i)
#     instance_id.append(i.id)

# print(ec2_resource.instances.filter(InstanceIds=instance_id).terminate())
insts_ids = []

# instances= ec2_client.describe_instances(Filters = [
#     {
#         "Name" : "instance-state-name",
#         "Values": ["running"]
#     }
# ] )
# # print(instances)

# # print(instances["Reservations"][0]["Instances"])
# for i in instances["Reservations"][0]["Instances"]:
#     print(i["InstanceId"])
#     insts_ids.append(i["InstanceId"])

# ec2_client.stop_instances(InstanceIds = insts_ids)

instance_response = ec2_client.run_instances(
    ImageId='ami-0ca2e925753ca2fb4',
    InstanceType='t2.micro',
    MaxCount=4,
    MinCount=4,
)
inst_ids=[]
for instance in instance_response["Instances"]:
    inst_ids.append(instance["InstanceId"])
    
waiter = ec2_client.get_waiter('instance_running')
waiter.wait(InstanceIds=inst_ids)
print("Instance ",inst_ids," Created")
# print(instance_response)
print("Instances created")