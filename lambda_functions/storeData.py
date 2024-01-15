import json
import boto3

def lambda_handler(event, context):
    
    table_name = 'parking_data'
    dynamodb = boto3.resource('dynamodb')
    table = dynamodb.Table(table_name)
        
    for e in event:
        key = e['date'] + '_' + e['time']
        try:
            response = table.put_item(
                Item={
                'fan': key,
                'value': e
            }
        )
        except Exception as e:
            return {
                'statusCode': 500,
                'body': f'Error: {str(e)}'
            }
       
    return_json = []     
    for i in range(7):
        return_json.append({
        'table': table_name,
        'weekday': i
    })
    
    return return_json