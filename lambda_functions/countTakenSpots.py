import json
import boto3


def lambda_handler(event, context):
    s3_bucket = event['Image']['S3Object']['Bucket']
    image_name = event['Image']['S3Object']['Name']
    plot_path = event['PlotPath']
    table = event['Table']
    total_spots = event['TotalSpots']

    rekognition = boto3.client('rekognition', region_name='us-east-1')

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
        'S3Bucket': s3_bucket,
        'PlotPath': plot_path,
        'Table': table,
        'TotalSpots': total_spots,
        'Taken': instances_count
    }
