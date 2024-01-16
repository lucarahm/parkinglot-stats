import json


def lambda_handler(event, context):
    s3_bucket = event['S3Bucket']
    plot_path = event['PlotPath']
    total_spots = event['TotalSpots']
    weekday = ['Weekday']
    data = ['Data']

    # TODO implement

    return "I LOVE DS!"