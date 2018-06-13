#! /usr/bin/python

#
# Author: Sharad Chhetri
# Date: 13-Jun-2018
# Blog: http://sharadchhetri.com
# Version: 1.0
# Description: This is basic script to create volume snapshot in AWS



#### PreReq ############
# 1. Set AWS Credentials - https://boto3.readthedocs.io/en/latest/guide/configuration.html
# 2. pip install boto3
########################
#
###################################################################
# To know about python command absolute path,run command -
# a=$(which python) && echo $a
###################################################################

#
# Note: do not forget to replace volume id in vol_id variable
#

import boto3
from datetime import dates

ec2 = boto3.client('ec2')
today = str(date.today())

vol_id = ['vol-123d67f90123456','vol-123d34455d456662']
for vol in vol_id:
    response = ec2.create_snapshot(
        Description='Sharad Chhetri Blog vol id:' + vol + ' Dated On:' + today,
        VolumeId=vol,
    )
    print(response)