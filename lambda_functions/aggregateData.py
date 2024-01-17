import json
import boto3


def lambda_handler(event, context):
    s3_bucket = event['S3Bucket']
    plot_path = event['PlotPath']
    table = event['Table']
    weekday = event['Weekday']
    total_spots = event['TotalSpots']

    dynamodb = boto3.resource('dynamodb')
    dbtable = dynamodb.Table(table)

    aggregatedData = []

    items = dbtable.scan()['Items']
    for item in items:
        itemValue = item['value']
        if (itemValue['Weekday'] != weekday):
            continue
        aggregation = {
            'Time': itemValue['Time'],
            'Taken': itemValue['Taken']
        }
        aggregatedData.append(aggregation)

    return {
        'S3Bucket': s3_bucket,
        'PlotPath': plot_path,
        'TotalSpots': total_spots,
        'Weekday': weekday,
        'Data': aggregatedData
    }