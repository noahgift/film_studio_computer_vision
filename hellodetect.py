#import boto3


def detect(bucket, name):
    #rekognition = boto3.client("rekognition")
    print(f"This is the bucket {bucket} and the name {name}")

detect("foo", "bar")