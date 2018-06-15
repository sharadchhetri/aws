#! /usr/bin/python

#
# Author: Sharad Chhetri
# Date: 15-Jun-2018
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

#### Things to do ####
# 1. Create a file and write vol id.
# example
#  vi /data/volume_list
#  vol-s0me12id
#  vol-skksjka2eeoi3l
#  vol-ejhwkjhe8888
#
# 2. In script, change the value in variable called 'filename ' and give absolute path of your vol id list file
# 3. Modify 'Description' variable as per your wish.
#
#


import boto3
from datetime import date

ec2 = boto3.client('ec2')
today = str(date.today())


filename = "/data/volume_list"


with open(filename) as f:
    content = f.read().splitlines()

for vol in content:
    response = ec2.create_snapshot(
        Description='Sharad Chhetri Blog vol id:' + vol + ' Dated On:' + today,
        VolumeId=vol,
    )
    print(response)