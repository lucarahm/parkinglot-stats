import json
import boto3

def lambda_handler(event, context):
    # Input should be S3 Bucket
    
    s3 = boto3.client('s3', region_name='us-east-1')
    bucket_name = 'dsprojecttestbucket'
    response = s3.list_objects(Bucket=bucket_name)
    image_keys = [obj['Key'] for obj in response.get('Contents', [])]
    
    return_json = []
    for key in image_keys:
        image  = {
            "Image": {
                "S3Object": {
                    "Bucket": bucket_name,
                    "Name": key
                }
            }
        }
        return_json.append(image)

    # Returns Array of all the images in the folder
    return return_json
