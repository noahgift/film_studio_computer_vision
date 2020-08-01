import boto3


def detect(bucket, name):
    client = boto3.client("rekognition")
    print(f"This is the bucket {bucket} and the name {name}")
    response = client.detect_labels(
        Image={"S3Object": {"Bucket": bucket, "Name": name,}}
    )
    return response

print(detect(bucket="netflix-film-studio", name="lebron-lakers.jpeg"))
