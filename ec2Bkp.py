import boto3
import botocore.exceptions
import json

ec2 = boto3.client('ec2')
s3 = boto3.client('s3')

def lambda_handler(event, context):
    instance_id = event['detail']['instance-id']
    bucket_name = 'ajays3bucket12'  # Replace with your S3 bucket name

    try:
        # Check if the instance state is 'shutting-down'
        state = event['detail']['state']
        if state == 'shutting-down':
            # Describe the instance
            instance = ec2.describe_instances(InstanceIds=[instance_id])
            # Convert the instance data to JSON
            instance_json = json.dumps(instance, default=str)
            # Save instance data to S3
            s3.put_object(Bucket=bucket_name, Key=f'ec2_instance_{instance_id}.json', Body=instance_json)
    except botocore.exceptions.ClientError as e:
        print(f"Error: {e}")

    return {
        'statusCode': 200,
        'body': 'Instance state saved to S3.'
    }
