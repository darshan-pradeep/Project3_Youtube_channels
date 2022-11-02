import boto3
import os


def s3_connector(download_title):
    s3=boto3.resource(
    service_name='s3',
    region_name='us-east-1',
    aws_access_key_id=os.environ['AWS_ACCESS_KEY_ID'],
    aws_secret_access_key=os.environ['AWS_SECRET_ACCESS_KEY']   
    )
    
    bucket_name=os.environ['AWS_BUCKET_NAME']
    s3.Bucket(bucket_name).download_file(Key=download_title,Filename=download_title)