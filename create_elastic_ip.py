# import the boto3 which will use to interact  with the aws
import boto3

REGION = input("Please enter the your REGION Name: ")
clientForIP = boto3.client('ec2', region_name=REGION)
domain_name = input("Please enter the your domain Name: ")
key = input("Please enter key value: ")
key_value = input("Please enter key value: ")
create = clientForIP.allocate_address(
    Domain=domain_name,
    TagSpecifications=[
        {
            'ResourceType': 'elastic-ip',
            'Tags': [
                {
                    'Key': key,
                    'Value': key_value
                },
            ]
        },
    ]
)

print(f'It is Done, Your allocation ID is {create["AllocationId"]}')
print(f'  - Wow, Your elastic IP {create["PublicIp"]} has been allocated')
print("Now you can use the IP")