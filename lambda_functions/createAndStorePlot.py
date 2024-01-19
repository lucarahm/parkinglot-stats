import json
import matplotlib.pyplot as plt
import datetime as Datetime
import io
import boto3
import numpy as np


def interpolate_data(time_array, taken_array):
    # Convert timeArray to hours
    hours = np.array([time.hour + time.minute / 60 for time in time_array])

    # Create new time values at hourly intervals
    new_hours = np.arange(np.floor(hours.min()), np.ceil(hours.max()) + 1)

    # Interpolate takenArray for the new time values using numpy's interp function
    new_taken_array = np.interp(new_hours, hours, taken_array, left=np.nan, right=np.nan)

    # Convert new_hours back to datetime
    new_time_array = [Datetime.time(int(hour), int((hour % 1) * 60)) for hour in new_hours]

    print(new_time_array)
    print(new_taken_array)

    return new_time_array, new_taken_array


def lambda_handler(event, context):
    s3_bucket = event['S3Bucket']
    plot_path = event['PlotPath']
    total_spots = event['TotalSpots']
    weekday = event['Weekday']
    data = event['Data']

    datetime = Datetime.datetime

    sorted_data = sorted(data, key=lambda x: datetime.strptime(x['Time'], '%H:%M'))

    time_array = [datetime.strptime(time['Time'], '%H:%M') for time in sorted_data]
    taken_array = [taken['Taken'] for taken in sorted_data]

    new_time_array, new_taken_array = interpolate_data(time_array, taken_array)

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    weekday_str = weekdays[weekday]

    plt.bar([str(t)[:5] for t in new_time_array], new_taken_array)
    plt.axhline(y=total_spots, color='red', linestyle='--', label='Threshold at 69')
    plt.gcf().autofmt_xdate()
    plt.title(f'Average Taken Spots for {weekday_str}')
    plt.xlabel('Time')
    plt.ylabel('Taken Spots')

    img_data = io.BytesIO()
    img_data.flush()
    plt.savefig(img_data, format='png')
    plt.close()
    img_data.flush()
    img_data.seek(0)

    s3 = boto3.resource('s3')
    bucket = s3.Bucket(s3_bucket)
    bucket.put_object(Body=img_data, ContentType='image/png', Key=f'{plot_path}/{weekday_str}.png')

    return "I LOVE DS!"