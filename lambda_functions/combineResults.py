import json


def lambda_handler(event, context):
    
    return {**event[0], **event[1]}
