import json
import boto3


def lambda_handler(event, context):
    bucket_name = event['S3Bucket']
    image_path = event['ImagePath']
    plot_path = event['PlotPath']
    table = event['Table']
    total_spots = event['TotalSpots']

    s3 = boto3.client('s3', region_name='us-east-1')

    response = s3.list_objects(Bucket=bucket_name, Prefix=image_path)
    image_keys = [obj['Key'] for obj in response.get('Contents', []) if not obj['Key'].endswith('/')]

    return_json = []
    for key in image_keys:
        image = {
            'Image': {
                'S3Object': {
                    'Bucket': bucket_name,
                    'ImagePath': image_path,
                    'Name': key,
                }
            },
            'PlotPath': plot_path,
            'TotalSpots': total_spots,
            'Table': table
        }
        return_json.append(image)

    # Returns Array of all the images in the folder
    return return_json
