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

    aggregated_data = {}
    count_data = {}

    items = dbtable.scan()['Items']
    for item in items:
        item_value = item['value']
        if (item_value['Weekday'] != weekday):
            continue

        time_value = item_value.get('Time')
        taken_value = item_value.get('Taken')

        if time_value in aggregated_data:
            aggregated_data[time_value]['Taken'] += taken_value
            count_data[time_value] += 1
        else:
            aggregated_data[time_value] = {'Time': time_value, 'Taken': taken_value}
            count_data[time_value] = 1

    for time_value, data in aggregated_data.items():
        data['Taken'] /= count_data[time_value]

    aggregated_data_list = list(aggregated_data.values())

    return {
        'S3Bucket': s3_bucket,
        'PlotPath': plot_path,
        'TotalSpots': total_spots,
        'Weekday': weekday,
        'Data': aggregated_data_list
    }