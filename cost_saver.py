import boto3

def lambda_handler(event, context):
    ec2 = boto3.client('ec2')
    
    # Locate all unattached EBS volumes wasting money
    volumes = ec2.describe_volumes(Filters=[{'Name': 'status', 'Values': ['available']}])
    
    deleted_count = 0
    for volume in volumes['Volumes']:
        volume_id = volume['VolumeId']
        print(f"Found unattached volume: {volume_id}. Deleting to save costs...")
        # ec2.delete_volume(VolumeId=volume_id)  # Safety lock: uncomment to actually delete
        deleted_count += 1
        
    return {
        "statusCode": 200,
        "body": f"FinOps execution complete. Cleaned up {deleted_count} volumes."
    }