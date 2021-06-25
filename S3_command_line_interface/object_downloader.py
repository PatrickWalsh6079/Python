# snippet-comment:[These are tags for the AWS doc team's sample catalog. Do not remove.]
# snippet-sourcedescription:[get_object.py demonstrates how to retrieve an object from an Amazon S3 bucket.]
# snippet-service:[s3]
# snippet-keyword:[Amazon S3]
# snippet-keyword:[Python]
# snippet-sourcesyntax:[python]
# snippet-sourcesyntax:[python]
# snippet-keyword:[Code Sample]
# snippet-sourcetype:[full-example]
# snippet-sourcedate:[2019-2-13]
# snippet-sourceauthor:[AWS]

# Copyright 2010-2019 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#
# This file is licensed under the Apache License, Version 2.0 (the "License").
# You may not use this file except in compliance with the License. A copy of the
# License is located at
#
# http://aws.amazon.com/apache2.0/
#
# This file is distributed on an "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS
# OF ANY KIND, either express or implied. See the License for the specific
# language governing permissions and limitations under the License.

import logging
import boto3
import botocore
from botocore.exceptions import ClientError


def download_object(bucket, key):
    
    # BUCKET_NAME = 'bucket1-week2' # replace with your bucket name
    # KEY = 'object_for_copy.txt' # replace with your object key
    
    s3 = boto3.resource('s3')
    
    try:
        s3.Bucket(bucket).download_file(key, '/home/ec2-user/environment/week_2/object_for_copy.txt')
        print('Successfully downloaded object object_for_copy.txt from bucket bucket1-week2')
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
