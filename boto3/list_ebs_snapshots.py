#! /usr/bin/python

#
# Author: Sharad Chhetri
# Date: 22-Jun-2018
# Blog: http://sharadchhetri.com
# Version: 1.0
# Description: This is basic script to create volume snapshot in AWS



#### PreReq ############
# 1. Set AWS Credentials - https://boto3.readthedocs.io/en/latest/guide/configuration.html
# 2. pip install boto3
########################
#
######################################

#############################
# To know about python command absolute path,run command -
# a=$(which python) && echo $a
###################################################################

#
# Note: do not forget to replace volume id in vol_id variable
#

import boto3

client = boto3.client('ec2')

response = client.describe_snapshots(OwnerIds=['self'])
list=response['Snapshots']

for i in list:
    print(i['SnapshotId'])
