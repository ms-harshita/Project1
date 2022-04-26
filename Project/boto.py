import boto3

        

def create_bucket(name):
    client = boto3.client('s3')
    response = client.create_bucket(Bucket=name)
   
    
    return (f"{name} bucket created successfully.")


def delete_bucket(name):

    client = boto3.client('s3')
    response = client.delete_bucket(Bucket=name)

   
    
    return (f"{name} bucket deleted successfully.")

    


def create_instance():
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    instances = ec2_client.run_instances(
        ImageId="ami-04505e74c0741db8d",
        MinCount=1,
        MaxCount=1,
        InstanceType="t2.micro"
    )

    print(instances["Instances"][0]["InstanceId"])

def terminate_ec2(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.terminate_instances(InstanceIds=[instance_id])
    return "terminated"
    
def stop_ec2(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.stop_instances(InstanceIds=[instance_id])
    return "stopped"


def start_ec2(instance_id):
    ec2_client = boto3.client("ec2", region_name="us-east-1")
    response = ec2_client.start_instances(InstanceIds=[instance_id])
    return "started" 
