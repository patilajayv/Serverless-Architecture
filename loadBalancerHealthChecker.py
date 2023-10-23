import boto3

def lambda_handler(event, context):
    elb_name = 'arn:aws:elasticloadbalancing:ap-south-1:295397358094:loadbalancer/app/adarsh-neeraj-lb/b75d821e7370c5cd'
    sns_topic_arn = 'arn:aws:sns:ap-south-1:295397358094:AJAYSNS'
    
    elb = boto3.client('elbv2')
    sns = boto3.client('sns')

    instances = elb.describe_target_health(TargetGroupArn=elb_name)
    
    unhealthy_instances = [instance for instance in instances['TargetHealthDescriptions'] if instance['TargetHealth']['State'] != 'healthy']

    if unhealthy_instances:
        message = "Unhealthy instances found behind the ELB:\n"
        for instance in unhealthy_instances:
            message += f"Instance ID: {instance['Target']['Id']}, Health State: {instance['TargetHealth']['State']}\n"
        
        sns.publish(
            TopicArn=sns_topic_arn,
            Subject="Unhealthy Instances Alert",
            Message=message
        )
    
    return {
        'statusCode': 200,
        'body': 'Health check completed.'
    }
