import boto3
import random
import requests
import socket

client = boto3.client('cloudwatch', region_name = 'us-east-1')

#Add your custom logic here to get number of users logged in
countOfUsersLoggedIn = float(random.randint(1,50))
print(countOfUsersLoggedIn)

hostname = socket.gethostname()
print(socket.gethostname())

response = client.put_metric_data(
    Namespace='MyProjectCustomMetrics',
    MetricData=[
        {
            'MetricName': 'NoOfUsersLoggedIn',
            'Dimensions': [
                {
                    'Name': 'Instance Name',
                    'Value': hostname
                },
            ],
            'Value': countOfUsersLoggedIn,
            'Unit': 'None'

        },
    ]
)                                                                                                                      









