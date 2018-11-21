# aws
AWS related stuff like Cloudformation, python boto3 scripts etc.  <br>
email: admin@sharadchhetri.com <br>
Blog: http://sharadchhetri.com

<H1>AWS Regions Code</H1>
<pre>
# aws ec2 describe-regions --output json
{
    "Regions": [
        {
            "Endpoint": "ec2.ap-south-1.amazonaws.com", 
            "RegionName": "ap-south-1"
        }, 
        {
            "Endpoint": "ec2.eu-west-3.amazonaws.com", 
            "RegionName": "eu-west-3"
        }, 
        {
            "Endpoint": "ec2.eu-west-2.amazonaws.com", 
            "RegionName": "eu-west-2"
        }, 
        {
            "Endpoint": "ec2.eu-west-1.amazonaws.com", 
            "RegionName": "eu-west-1"
        }, 
        {
            "Endpoint": "ec2.ap-northeast-2.amazonaws.com", 
            "RegionName": "ap-northeast-2"
        }, 
        {
            "Endpoint": "ec2.ap-northeast-1.amazonaws.com", 
            "RegionName": "ap-northeast-1"
        }, 
        {
            "Endpoint": "ec2.sa-east-1.amazonaws.com", 
            "RegionName": "sa-east-1"
        }, 
        {
            "Endpoint": "ec2.ca-central-1.amazonaws.com", 
            "RegionName": "ca-central-1"
        }, 
        {
            "Endpoint": "ec2.ap-southeast-1.amazonaws.com", 
            "RegionName": "ap-southeast-1"
        }, 
        {
            "Endpoint": "ec2.ap-southeast-2.amazonaws.com", 
            "RegionName": "ap-southeast-2"
        }, 
        {
            "Endpoint": "ec2.eu-central-1.amazonaws.com", 
            "RegionName": "eu-central-1"
        }, 
        {
            "Endpoint": "ec2.us-east-1.amazonaws.com", 
            "RegionName": "us-east-1"
        }, 
        {
            "Endpoint": "ec2.us-east-2.amazonaws.com", 
            "RegionName": "us-east-2"
        }, 
        {
            "Endpoint": "ec2.us-west-1.amazonaws.com", 
            "RegionName": "us-west-1"
        }, 
        {
            "Endpoint": "ec2.us-west-2.amazonaws.com", 
            "RegionName": "us-west-2"
        }
    ]
}

</pre>

<pre>
# aws ec2 describe-regions --output text

REGIONS	ec2.ap-south-1.amazonaws.com	ap-south-1
REGIONS	ec2.eu-west-3.amazonaws.com	eu-west-3
REGIONS	ec2.eu-west-2.amazonaws.com	eu-west-2
REGIONS	ec2.eu-west-1.amazonaws.com	eu-west-1
REGIONS	ec2.ap-northeast-2.amazonaws.com	ap-northeast-2
REGIONS	ec2.ap-northeast-1.amazonaws.com	ap-northeast-1
REGIONS	ec2.sa-east-1.amazonaws.com	sa-east-1
REGIONS	ec2.ca-central-1.amazonaws.com	ca-central-1
REGIONS	ec2.ap-southeast-1.amazonaws.com	ap-southeast-1
REGIONS	ec2.ap-southeast-2.amazonaws.com	ap-southeast-2
REGIONS	ec2.eu-central-1.amazonaws.com	eu-central-1
REGIONS	ec2.us-east-1.amazonaws.com	us-east-1
REGIONS	ec2.us-east-2.amazonaws.com	us-east-2
REGIONS	ec2.us-west-1.amazonaws.com	us-west-1
REGIONS	ec2.us-west-2.amazonaws.com	us-west-2

</pre>

<H1>AWS - prefix-lists </H1>

<pre>
# for i in $(aws ec2 describe-regions --query 'Regions[].{Name:RegionName}' --output text);do aws --region $i ec2 describe-prefix-lists --output json;done

{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.ap-south-1.s3", 
            "Cidrs": [
                "52.92.248.0/22", 
                "52.219.62.0/23", 
                "52.219.64.0/22"
            ], 
            "PrefixListId": "pl-78a54011"
        }, 
        {
            "PrefixListName": "com.amazonaws.ap-south-1.dynamodb", 
            "Cidrs": [
                "52.94.20.0/24"
            ], 
            "PrefixListId": "pl-66a7420f"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.eu-west-3.dynamodb", 
            "Cidrs": [
                "52.94.16.0/24"
            ], 
            "PrefixListId": "pl-abb451c2"
        }, 
        {
            "PrefixListName": "com.amazonaws.eu-west-3.s3", 
            "Cidrs": [
                "52.95.154.0/23", 
                "52.95.156.0/24"
            ], 
            "PrefixListId": "pl-23ad484a"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.eu-west-2.dynamodb", 
            "Cidrs": [
                "52.94.15.0/24"
            ], 
            "PrefixListId": "pl-b3a742da"
        }, 
        {
            "PrefixListName": "com.amazonaws.eu-west-2.s3", 
            "Cidrs": [
                "52.95.150.0/24", 
                "52.92.88.0/22", 
                "52.95.148.0/23"
            ], 
            "PrefixListId": "pl-7ca54015"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.eu-west-1.dynamodb", 
            "Cidrs": [
                "52.94.5.0/24", 
                "52.119.240.0/21", 
                "52.94.24.0/23"
            ], 
            "PrefixListId": "pl-6fa54006"
        }, 
        {
            "PrefixListName": "com.amazonaws.eu-west-1.s3", 
            "Cidrs": [
                "52.218.0.0/17", 
                "54.231.128.0/19"
            ], 
            "PrefixListId": "pl-6da54004"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.ap-northeast-2.dynamodb", 
            "Cidrs": [
                "52.94.6.0/24"
            ], 
            "PrefixListId": "pl-48a54021"
        }, 
        {
            "PrefixListName": "com.amazonaws.ap-northeast-2.s3", 
            "Cidrs": [
                "52.92.0.0/20", 
                "52.219.60.0/23", 
                "52.219.56.0/22"
            ], 
            "PrefixListId": "pl-78a54011"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.ap-northeast-1.dynamodb", 
            "Cidrs": [
                "52.94.8.0/24"
            ], 
            "PrefixListId": "pl-78a54011"
        }, 
        {
            "PrefixListName": "com.amazonaws.ap-northeast-1.s3", 
            "Cidrs": [
                "52.219.0.0/20", 
                "54.231.224.0/21", 
                "52.219.16.0/22", 
                "52.219.68.0/22"
            ], 
            "PrefixListId": "pl-61a54008"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.sa-east-1.dynamodb", 
            "Cidrs": [
                "52.94.7.0/24"
            ], 
            "PrefixListId": "pl-60a54009"
        }, 
        {
            "PrefixListName": "com.amazonaws.sa-east-1.s3", 
            "Cidrs": [
                "52.95.138.0/24", 
                "52.92.64.0/22", 
                "52.95.163.0/24", 
                "52.95.136.0/23", 
                "52.92.72.0/22", 
                "52.95.164.0/23"
            ], 
            "PrefixListId": "pl-6aa54003"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.ca-central-1.dynamodb", 
            "Cidrs": [
                "52.94.14.0/24"
            ], 
            "PrefixListId": "pl-4ea54027"
        }, 
        {
            "PrefixListName": "com.amazonaws.ca-central-1.s3", 
            "Cidrs": [
                "52.95.146.0/23", 
                "52.95.145.0/24", 
                "52.92.84.0/22"
            ], 
            "PrefixListId": "pl-7da54014"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.ap-southeast-1.s3", 
            "Cidrs": [
                "52.219.32.0/21", 
                "52.219.40.0/22", 
                "54.231.240.0/22", 
                "52.219.76.0/22"
            ], 
            "PrefixListId": "pl-6fa54006"
        }, 
        {
            "PrefixListName": "com.amazonaws.ap-southeast-1.dynamodb", 
            "Cidrs": [
                "52.94.11.0/24"
            ], 
            "PrefixListId": "pl-67a5400e"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.ap-southeast-2.s3", 
            "Cidrs": [
                "54.231.248.0/22", 
                "54.231.252.0/24", 
                "52.95.128.0/21"
            ], 
            "PrefixListId": "pl-6ca54005"
        }, 
        {
            "PrefixListName": "com.amazonaws.ap-southeast-2.dynamodb", 
            "Cidrs": [
                "52.94.13.0/24"
            ], 
            "PrefixListId": "pl-62a5400b"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.eu-central-1.s3", 
            "Cidrs": [
                "52.219.44.0/22", 
                "54.231.192.0/20", 
                "52.219.72.0/22"
            ], 
            "PrefixListId": "pl-6ea54007"
        }, 
        {
            "PrefixListName": "com.amazonaws.eu-central-1.dynamodb", 
            "Cidrs": [
                "52.94.17.0/24"
            ], 
            "PrefixListId": "pl-66a5400f"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.us-east-1.s3", 
            "Cidrs": [
                "54.231.0.0/17", 
                "52.216.0.0/15"
            ], 
            "PrefixListId": "pl-63a5400a"
        }, 
        {
            "PrefixListName": "com.amazonaws.us-east-1.dynamodb", 
            "Cidrs": [
                "52.94.0.0/22", 
                "52.119.224.0/20"
            ], 
            "PrefixListId": "pl-02cd2c6b"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.us-east-2.dynamodb", 
            "Cidrs": [
                "52.94.4.0/24"
            ], 
            "PrefixListId": "pl-4ca54025"
        }, 
        {
            "PrefixListName": "com.amazonaws.us-east-2.s3", 
            "Cidrs": [
                "52.219.80.0/20", 
                "52.219.96.0/20", 
                "52.92.76.0/22"
            ], 
            "PrefixListId": "pl-7ba54012"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.us-west-1.s3", 
            "Cidrs": [
                "52.219.20.0/22", 
                "54.231.232.0/21", 
                "52.219.24.0/21", 
                "52.92.48.0/22"
            ], 
            "PrefixListId": "pl-6ba54002"
        }, 
        {
            "PrefixListName": "com.amazonaws.us-west-1.dynamodb", 
            "Cidrs": [
                "52.94.12.0/24"
            ], 
            "PrefixListId": "pl-6ea54007"
        }
    ]
}
{
    "PrefixLists": [
        {
            "PrefixListName": "com.amazonaws.us-west-2.s3", 
            "Cidrs": [
                "54.231.160.0/19", 
                "52.218.128.0/17", 
                "52.92.32.0/22"
            ], 
            "PrefixListId": "pl-68a54001"
        }, 
        {
            "PrefixListName": "com.amazonaws.us-west-2.dynamodb", 
            "Cidrs": [
                "52.94.28.0/23"
            ], 
            "PrefixListId": "pl-00a54069"
        }
    ]
}

</pre>
