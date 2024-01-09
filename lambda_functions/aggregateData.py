import json


def lambda_handler(event, context):
    # TODO implement
    return {
        'total': 400,
        'weekday': "Mon",
        'data':
            [{'time': "12:50", 'empty': 221}, {'time': "13:00", 'empty': 220}]
    }
