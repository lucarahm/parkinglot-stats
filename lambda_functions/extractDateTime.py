import json
from datetime import datetime

def lambda_handler(event, context):
    
    # use in production environment
    # image_name = event['Image']['S3Object']['Name']
    
    image_name = '2012-09-12_06_36_36_jpg.rf.08869047c7e9f62f5ce9334546b52958.jpg'
    
    # Extracting date and time components
    date_str = image_name[:10]
    time_str = image_name[11:19].replace('_', ':')
    
    # 0 for monday
    weekday =  datetime.strptime(date_str, '%Y-%m-%d').date().weekday()
    
    return {
        "date": date_str,
        "time": time_str,
        "weekday": weekday
    }
