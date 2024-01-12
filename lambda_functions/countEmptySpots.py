import json
import boto3


def lambda_handler(event, context):
    
    rekognition = boto3.client('rekognition', 
        region_name='us-east-1')
    
    # used to simulate event input 
    #event = {
    #    'Image':{
    #        'S3Object': {
    #            'Bucket': 'dsprojecttestbucket',
    #            'Name': '2012-09-12_06_36_36_jpg.rf.08869047c7e9f62f5ce9334546b52958.jpg'
    #        }
    #    }
    #}
    
    s3_bucket = event['Image']['S3Object']['Bucket']
    image_name = event['Image']['S3Object']['Name']
    
    response = rekognition.detect_labels(
        Image={
            'S3Object': {
                'Bucket': s3_bucket,
                'Name': image_name
            }
        }
    )
    
    target_labels = ['Car', 'Motorcycle']
    instances_count = 0
    for target_label in target_labels:
        for label in response['Labels']:
            if label['Name'] == target_label:
                instances_count += len(label.get('Instances', []))

    # Print the instances count
    print(f"The labels '{target_labels}' appears {instances_count} times in the image.")
    
    return {
        'total': 47,
        'taken': instances_count
    }
