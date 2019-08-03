#!/usr/bin/python
#
# Author: Sharad Chhetri
# Date: 03/Jul/2019
# Blog: http://sharadchhetri.com
# Version: 1.0
# Description: This is a basic python script to list s3 bucket in AWS. We are using the module called boto3.

#### PreReq ############
# 1. Set AWS Credentials - https://boto3.readthedocs.io/en/latest/guide/configuration.html
# 2. pip install boto3
########################
#############################
# To know about python command absolute path,run command -
# a=$(which python) && echo $a
###################################################################


import boto3

client = boto3.client('s3')
response = client.list_buckets()

for i in response['Buckets']:
    print(i['Name'])
