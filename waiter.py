import boto3
ec2_session=boto3.session.Session(profile_name="applicationDev")
ec2_conn=ec2_session.client('ec2')
print("Starting Ec2 Instance")
ec2_conn.start_instances(InstanceIds=['i-094517a40c9624cfd'])
waiter = ec2_conn.get_waiter('instance_running')
waiter.wait(InstanceIds=['i-094517a40c9624cfd'])
print("Starting Ec2 Instance")