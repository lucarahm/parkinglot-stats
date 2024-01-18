import json
import matplotlib.pyplot as plt
import datetime as Datetime
import io


def lambda_handler(event, context):
    datetime = Datetime.datetime

    input = {
        "weekday": "2",
        "Data": [
            {
                "Time": "08:00",
                "Taken": 20
            },
            {
                "Time": "09:00",
                "Taken": 30
            },
            {
                "Time": "10:00",
                "Taken": 40
            },
            {
                "Time": "11:00",
                "Taken": 30
            },
            {
                "Time": "12:00",
                "Taken": 40
            },
            {
                "Time": "12:00",
                "Taken": 60
            }
        ]
    }

    timeArray = [datetime.strptime(time['Time'], '%H:%M') for time in input["Data"]]
    takenArray = [taken['Taken'] for taken in input["Data"]]
    print(timeArray)
    print(takenArray)

    plt.plot(timeArray, takenArray)
    plt.gcf().autofmt_xdate()
    # plt.show()

    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)

    s3 = boto3.resource('s3')
    bucket = s3.Bucket('ds-plot-bucket')
    bucket.put_object(Body=img_data, ContentType='image/png', Key='plot.png')

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
