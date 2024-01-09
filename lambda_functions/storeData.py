import json


def lambda_handler(event, context):
    # TODO implement
    return [{
        'databaseURI': "redis",
        'weekday': "Monday"
    },
    {
        'databaseURI': "redis",
        'weekday': "Tuesday"
    },
    {
        'databaseURI': "redis",
        'weekday': "Wed"
    },
    {
        'databaseURI': "redis",
        'weekday': "Thu"
    },
    {
        'databaseURI': "redis",
        'weekday': "Fri"
    },
    {
        'databaseURI': "redis",
        'weekday': "Sat"
    },
    {
        'databaseURI': "redis",
        'weekday': "S"
    }]
