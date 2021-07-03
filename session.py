import boto3
import pprint
ec2_session=boto3.session.Session(profile_name="applicationDev")
ec2_conn=ec2_session.client('ec2')
response=ec2_conn.describe_hosts()
pprint(response)