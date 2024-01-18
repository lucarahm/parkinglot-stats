import json
import matplotlib.pyplot as plt
import datetime as Datetime
import io
import boto3


def lambda_handler(event, context):
    s3_bucket = event['S3Bucket']
    plot_path = event['PlotPath']
    total_spots = event['TotalSpots']
    weekday = event['Weekday']
    data = event['Data']

    datetime = Datetime.datetime

    timeArray = sorted([datetime.strptime(time['Time'], '%H:%M') for time in data])
    takenArray = [taken['Taken'] for taken in data]

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_str = weekdays[weekday]

    plt.plot(timeArray, takenArray)
    plt.gcf().autofmt_xdate()
    # plt.show()

    img_data = io.BytesIO()
    plt.savefig(img_data, format='png')
    img_data.seek(0)

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(s3_bucket)
    bucket.put_object(Body=img_data, ContentType='image/png', Key=f'{plot_path}/{weekday_str}')

    return "I LOVE DS!"