import json


def lambda_handler(event, context):
    # Input should be S3 Bucket

    # Returns Array of all the images in the folder

    return [{
        "Image": {
            "S3Object": {
                "Bucket": "rekognition-console-v4-prod-iad",
                "Name": "assets/StaticImageAssets/SampleImages/skateboard.jpg"
            }
        }
    }]
