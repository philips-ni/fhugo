+++
title = "Sample-Tracker API Testing"
author = ["Fei Ni"]
date = 2021-07-16T18:07:07-07:00
lastmod = 2021-07-16T18:07:07-07:00
tags = ["helix"]
categories = ["helix"]
draft = false
+++

## <span class="section-num">1</span> Clear Samples {#clear-samples}

```bash
tableName=SampleTrackerSamples
export KEY_SCHEMA=$(aws dynamodb describe-table  --table-name ${tableName} | jq -r '.Table.KeySchema[].AttributeName')
echo $KEY_SCHEMA

aws dynamodb scan \
    --table-name ${tableName} \
    --attributes-to-get ${KEY_SCHEMA} | \
    jq -r ".Items[] | tojson" | \
    tr '\n' '\0' | \
    xargs -0 -I keyItem \
	  aws dynamodb delete-item \
	  --table-name ${tableName} \
	  --key=keyItem

```


## <span class="section-num">2</span> Import Samples {#import-samples}

```bash
$ curl -H 'X-Auth-Token-Internal: IS-XXXXX' -H 'X-Auth-Caller-Internal: myhealth-workflow' -H 'Content-Type: application/json' --request POST -d@postData https://ob5m8axfye.execute-api.us-east-1.amazonaws.com/v1/samples

# cat postData
{
  "samples":[
    {
      "kitID": "KIT-001",
      "testCode": "TC-001",
      "VRC": "VRC-001"
    },
    {
      "kitID": "KIT-002",
      "testCode": "TC-002",
      "VRC": "VRC-002"
    }
  ]
}
```


## <span class="section-num">3</span> List Samples {#list-samples}

```bash
$ curl https://ob5m8axfye.execute-api.us-east-1.amazonaws.com/v1/info?info_type=sample&state=pending

$ curl https://ob5m8axfye.execute-api.us-east-1.amazonaws.com/v1/info?info_type=sample&samleID=XXX&coID=XXX
```


## <span class="section-num">4</span> List Orders {#list-orders}

```bash
$ curl -v https://ob5m8axfye.execute-api.us-east-1.amazonaws.com/v1/info?info_type=order
```


## <span class="section-num">5</span> Deal with users {#deal-with-users}

```python
import boto3
from boto3.dynamodb.conditions import Key

dynamodb = boto3.resource('dynamodb')

table = dynamodb.Table('SampleTrackerUsers')


def list_users():
    resp = table.scan()
    print("=========List Users==================")
    for item in resp['Items']:
	print(item["UserID"])


def add_user(user_email):
    item = {
	"UserID": user_email,
	"Role": "Staff"
    }
    table.put_item(Item=item)
    print("\n!!! {} is added".format(user_email))

def add_users(users):
    for user in users:
	add_user(user)


def del_user(user_email):
    key = {
	"UserID": user_email
    }
    table.delete_item(Key=key)
    print("\n!!! {} is deleted".format(user_email))


def del_users(users):
    for user in users:
	del_user(user)


users = [
    "fei.ni@helix.com"
]

list_users()
del_users(users)
list_users()
add_users(users)
list_users()
```
