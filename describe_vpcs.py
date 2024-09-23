import boto3
import os

region = os.environ['AWS_REGION']
print('Default Region Set: ', region)
ec2 = boto3.client('ec2', region_name = region)
vpc_list = ec2.describe_vpcs()
print(vpc_list)
