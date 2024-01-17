import json
from datetime import datetime


def lambda_handler(event, context):
    image_name = event['Image']['S3Object']['Name']
    path = event['Image']['S3Object']['ImagePath']

    # remove path from the file name to extract date and time
    image_name = image_name.replace(path, '').replace('/', '')

    # Extracting date and time components
    date_str = image_name[:10]
    time_str = image_name[11:16].replace('_', ':')

    # 0 for monday
    weekday = datetime.strptime(date_str, '%Y-%m-%d').date().weekday()

    return {
        'Date': date_str,
        'Time': time_str,
        'Weekday': weekday
    }
