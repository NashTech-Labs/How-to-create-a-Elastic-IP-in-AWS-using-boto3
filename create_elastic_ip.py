# import the boto3 which will use to interact  with the aws
import boto3

AWS_REGION = input("Enter the AWS_REGION Name")
EC2_CLIENT = boto3.client('ec2', region_name=AWS_REGION)

allocation = EC2_CLIENT.allocate_address(
    Domain='vpc',
    TagSpecifications=[
        {
            'ResourceType': 'elastic-ip',
            'Tags': [
                {
                    'Key': 'Name',
                    'Value': 'tech_hub-elastic-ip'
                },
            ]
        },
    ]
)

print(f'It is Done, Your allocation ID is {allocation["AllocationId"]}')
print(f'  - Wow, Your elastic IP {allocation["PublicIp"]} has been allocated')
print("Now you can use the IP")