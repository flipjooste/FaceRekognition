from boto3 import client
import boto3

# Create an S3 client
s3 = boto3.client('s3')
conn = client('s3')  # again assumes boto.cfg setup, assume AWS S3

# Call S3 to list current buckets
response = s3.list_buckets()
print(response)
found = 0
# Get a list of all bucket names from the response
for bucket in response['Buckets']:
    print(bucket['Name'])
    if found == 1:
        break
    try:
        for key in conn.list_objects(Bucket=bucket['Name'])['Contents']:
            if key['Key'] == 'MG_HF7S9Z_20180911_101950.JPG':
                print('found')
                print(bucket['Name'])
                found = 1
                break
    except:
        print('error')