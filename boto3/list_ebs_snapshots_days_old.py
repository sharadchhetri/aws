#! /usr/bin/python

#
# Author: Sharad Chhetri
# Date: 05-Jul-2018
# Blog: http://sharadchhetri.com
# Version: 1.0
# Description: This is basic script to list snapshot ids older than some particular days in AWS
#



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
# In (OwnerIds=['self'] , you can replace 'self' with 'AWS Account number'
#
#
import boto3
import collections
import datetime
import time
import sys

# Mention how many days ago old snapshot id should be listed
days_ago = 60

client = boto3.client('ec2')

response = client.describe_snapshots(OwnerIds=['self'])
list=response['Snapshots']

#
# This for loop block will print all snapshots id , Volume id and snapshot creation time.
#
#for i in list:
#    print(i['SnapshotId'],i['VolumeId'],i['StartTime'])
#

today = datetime.datetime.now()
today_f = today.strftime('%Y-%m-%d')
ago = datetime.datetime.now() - datetime.timedelta(days=days_ago)
ago_f = ago.strftime('%Y-%m-%d')

for j in list:
    snp = j['StartTime']
    snp_f = snp.strftime('%Y-%m-%d')
    if snp_f < ago_f:
        print(j['SnapshotId'], j['VolumeId'], snp_f)
