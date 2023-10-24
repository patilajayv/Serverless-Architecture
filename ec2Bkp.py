import boto3
import botocore.exceptions
import json

ec2 = boto3.client('ec2', region_name='ap-south-1')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    bucket_name = 'ajays3bucket12'

    try:
        instances = ec2.describe_instances(Filters=[{'Name': 'instance-state-name', 'Values': ['running', 'shutting-down']}])
        
        for reservation in instances['Reservations']:
            for instance in reservation['Instances']:
                instance_id = instance['InstanceId']
                state = instance['State']['Name']
                
                if state == 'shutting-down':
                    instance_json = json.dumps(instance, default=str)
                    s3.put_object(Bucket=bucket_name, Key=f'ec2_instance_{instance_id}.json', Body=instance_json)
                    
        return {
            'statusCode': 200,
            'body': 'Instance states saved to S3.'
        }
    
    except botocore.exceptions.ClientError as e:
        print(f"Error: {e}")
        return {
            'statusCode': 500,
            'body': 'Error occurred while checking instance states.'
        }
