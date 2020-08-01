"""Full Event Driven Lambda with Label Detection"""

import boto3
from urllib.parse import unquote_plus

def detect(bucket, name):
    client = boto3.client("rekognition")
    print(f"This is the bucket {bucket} and the name {name}")
    response = client.detect_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": name,}}
    )
    return response
    
def lambda_handler(event, context):
    """This is a computer vision lambda handler"""

    print(f"This is my S3 event {event}")
    for record in event['Records']:
        bucket = record['s3']['bucket']['name']
        print(f"This is my bucket {bucket}")
        key = unquote_plus(record['s3']['object']['key'])
        print(f"This is my key {key}")
        
    my_labels = detect(bucket=bucket, 
        name=key)
    return my_labels