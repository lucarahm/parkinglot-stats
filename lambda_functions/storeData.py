import json
import boto3


def lambda_handler(event, context):
    s3_bucket = event[0]['S3Bucket']
    plot_path = event[0]['PlotPath']
    table = event[0]['Table']
    total_spots = event[0]['TotalSpots']

    dynamodb = boto3.resource('dynamodb')
    dbtable = dynamodb.Table(table)

    for e in event:
        key = e['Date'] + '_' + e['Time']
        value = {
            'Date': e['Date'],
            'Time': e['Time'],
            'Weekday': e['Weekday'],
            'TotalSpots': e['TotalSpots'],
            'Taken': e['Taken']
        }
        response = dbtable.put_item(
            Item={
                'fan': key,
                'value': value
            }
        )

    return_json = []
    for i in range(7):
        return_json.append({
            'S3Bucket': s3_bucket,
            'PlotPath': plot_path,
            'Table': table,
            'Weekday': i,
            'TotalSpots': total_spots
        })

    return return_json