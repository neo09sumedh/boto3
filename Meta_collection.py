import boto3
from pprint import pprint
ec2_session=boto3.session.Session(profile_name="applicationDev")
ec2_conn=ec2_session.resource(service_name='ec2')
f1={"Name":'instance-state-name',"Values":['stopped']}
intanceid=[]
for each_instance in ec2_conn.instances.filter(Filters=[f1]):
    intanceid.append(each_instance.id)
    
waiter=ec2_conn.meta.client.get_waiter('instance_running')
print("starting Instance")
ec2_conn.meta.client.start_instances(InstanceIds=intanceid)
waiter.wait(InstanceIds=intanceid)
print("All Instance Started")