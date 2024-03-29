# snippet-comment:[These are tags for the AWS doc team's sample catalog. Do not remove.]
# snippet-sourcedescription:[delete_bucket.py demonstrates how to delete an empty Amazon S3 bucket.]
# snippet-service:[s3]
# snippet-keyword:[Amazon S3]
# snippet-keyword:[Python]
# snippet-sourcesyntax:[python]
# snippet-sourcesyntax:[python]
# snippet-keyword:[Code Sample]
# snippet-sourcetype:[full-example]
# snippet-sourcedate:[2019-2-12]
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
from botocore.exceptions import ClientError


def delete_bucket(bucket_name):
    """Delete an empty S3 bucket

    If the bucket is not empty, the operation fails.

    :param bucket_name: string
    :return: True if the referenced bucket was deleted, otherwise False
    """

    # Delete the bucket
    s3 = boto3.client('s3')
    s3_resource = boto3.resource('s3')
    try:
        bucket = s3_resource.Bucket(bucket_name)
        bucket.objects.all().delete()
        s3.delete_bucket(Bucket=bucket_name)
        print('Successfully deleted bucket ' + bucket_name)
    except ClientError as e:
        logging.error(e)
        return False
    return True
