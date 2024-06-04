import boto3
from rich import print

session = boto3.Session(region_name="us-east-2")

ec2 = session.resource("ec2")

instances = ec2.instances.filter(
    Filters = [
        {
            "Name" : "instance-state-name",
            "Values": ["running"]
        }
    ]
)

all_volume_details = []
volume_ids = []
instance_ids = []
instances_and_volume_details = []

for i in instances: 
    # print(i.block_device_mappings)
    all_volume_details.append(i.block_device_mappings)
    # print(dir(i.block_device_mappings))
    instance_ids.append(i.id)
       
    details_of_instance = {
        "instance_id" : i.id,
        "volumes_details" : i.block_device_mappings
    }
    instances_and_volume_details.append(details_of_instance)

for volumes_per_instance in all_volume_details:
    # print(volumes_per_instance)
    for volume in volumes_per_instance:
        # print(volume["Ebs"]["VolumeId"])
        volume_ids.append(volume["Ebs"]["VolumeId"])

# print(instances_and_volume_details)

print("The volume id to take snapshot", volume_ids)

for id in volume_ids:
    snapshot_response = ec2.meta.client.create_snapshot(
        Description='Automated snapshot creation from python boto3 class',
        VolumeId=id
    )
    waiter = ec2.meta.client.get_waiter('snapshot_completed')
    waiter.wait(SnapshotIds=[snapshot_response["SnapshotId"]])

    print(snapshot_response)

print("Snapshot created")