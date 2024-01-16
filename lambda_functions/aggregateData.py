import json


def lambda_handler(event, context):
    s3_bucket = event['S3Bucket']
    plot_path = event['PlotPath']
    table = event['Table']
    weekday = event['Weekday']
    total_spots = event['TotalSpots']

    # TODO implement

    return {
        'S3Bucket': s3_bucket,
        'PlotPath': plot_path,
        'TotalSpots': total_spots,
        'Weekday': weekday,
        'Data': [
            {'Time': '12:50', 'Taken': 21},
            {'Time': '13:00', 'Taken': 19},
            {'Time': '13:10', 'Taken': 24}
        ]
    }
