# snippet-comment:[These are tags for the AWS doc team's sample catalog. Do not remove.]
# snippet-sourcedescription:[copy_object.py demonstrates how to copy an Amazon S3 bucket object.]
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


def copy_object(src_bucket_name, src_object_name,
                dest_bucket_name, dest_object_name=None):
    """Copy an Amazon S3 bucket object

    :param src_bucket_name: string
    :param src_object_name: string
    :param dest_bucket_name: string. Must already exist.
    :param dest_object_name: string. If dest bucket/object exists, it is
    overwritten. Default: src_object_name
    :return: True if object was copied, otherwise False
    """

    # Construct source bucket/object parameter
    copy_source = {'Bucket': src_bucket_name, 'Key': src_object_name}
    if dest_object_name is None:
        dest_object_name = src_object_name

    # Copy the object
    s3 = boto3.client('s3')
    try:
        s3.copy_object(CopySource=copy_source, Bucket=dest_bucket_name,
                       Key=dest_object_name)
        print('Successfully copied object object_for_copy.txt from bucket bucket1-week2 to bucket bucket2-week2')
    except ClientError as e:
        logging.error(e)
        return False
    return True
    