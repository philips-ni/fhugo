+++
title = "AWS tips"
author = ["Fei Ni"]
date = 2021-01-01
lastmod = 2022-02-07T09:29:24-08:00
tags = ["helix"]
categories = ["helix"]
draft = false
+++

## <span class="section-num">1</span> DNS {#dns}

-   <https://aws.amazon.com/premiumsupport/knowledge-center/cloudfront-domain-https/>


## <span class="section-num">2</span> IAMS {#iams}

-   <https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial%5Fcross-account-with-roles.html>


## <span class="section-num">3</span> CDK {#cdk}


### <span class="section-num">3.1</span> cross account permission grant {#cross-account-permission-grant}

Requirement:

```bash
Athena service is running in master account,
STT import lambda is running in hipaa-staging account

STT import lambda want to query data in Athena service.

```

The idea is :

-   create a role in `master` account which defines the policy to allow to query `Athena`
-   in CDK of `STT import lambda` grant the permission to assume the role which is created in #1
-   In `STT import lambda` golang code, before querying `Athena`, running assumeRole to get the temporarily access
-   <https://docs.aws.amazon.com/IAM/latest/UserGuide/tutorial%5Fcross-account-with-roles.html>
-   <https://aws.amazon.com/premiumsupport/knowledge-center/access-denied-athena/>


#### <span class="section-num">3.1.1</span> About implementation of `assumeRole` {#about-implementation-of-assumerole}


#### <span class="section-num">3.1.2</span> policy example {#policy-example}

```bash
{
    "Version": "2012-10-17",
    "Statement": [
	{
	    "Effect": "Allow",
	    "Action": [
		"athena:GetQueryExecution",
		"athena:StartQueryExecution",
		"athena:ListDatabases",
		"athena:ListPreparedStatements",
		"athena:ListNamedQueries"
	    ],
	    "Resource": "arn:aws:athena:us-east-1:820411415250:workgroup/primary"
	},
	{
	    "Effect": "Allow",
	    "Action": [
		"glue:GetTable"
	    ],
	    "Resource": [
		"arn:aws:glue:us-east-1:820411415250:catalog",
		"arn:aws:glue:us-east-1:820411415250:database/lims_db_staging",
		"arn:aws:glue:us-east-1:820411415250:table/lims_db_staging/*"
	    ]
	},
	{
	    "Effect": "Allow",
	    "Action": [
		"athena:ListDataCatalogs",
		"athena:ListWorkGroups"
	    ],
	    "Resource": "*"
	},
	{
	    "Effect": "Allow",
	    "Action": [
		"s3:ListAllMyBuckets",
		"s3:GetBucketLocation"
	    ],
	    "Resource": "*"
	},
	{
	    "Effect": "Allow",
	    "Action": [
		"s3:List*"
	    ],
	    "Resource": [
		"arn:aws:s3:::helix-lims-backup",
		"arn:aws:s3:::aws-athena-query-results-820411415250-us-east-1"
	    ]
	},
	{
	    "Effect": "Allow",
	    "Action": [
		"s3:GetObject",
		"s3:PutObject",
		"s3:AbortMultipartUpload",
		"s3:ListMultipartUploadParts"
	    ],
	    "Resource": [
		"arn:aws:s3:::helix-lims-backup/staging/*",
		"arn:aws:s3:::aws-athena-query-results-820411415250-us-east-1/staging/*"
	    ]
	}
    ]
}
```


## <span class="section-num">4</span> ECR {#ecr}


### <span class="section-num">4.1</span> ECR login {#ecr-login}

```bash

[fei.ni@fei-ni-C02FG3R2MD6N-SM master-dev helix-py-app-r2v (master %)]$ cat ecr_login
aws ecr get-login-password \
	--region us-east-1 | docker login \
		--username AWS \
			--password-stdin 820411415250.dkr.ecr.us-east-1.amazonaws.com
```


## <span class="section-num">5</span> Redshift & Glue {#redshift-and-glue}

-   <https://aws.amazon.com/blogs/big-data/analyze-your-amazon-s3-spend-using-aws-glue-and-amazon-redshift/>
-   <https://hevodata.com/learn/spark-vs-redshift/>
-   <https://aws.amazon.com/blogs/big-data/introducing-aws-glue-3-0-with-optimized-apache-spark-3-1-runtime-for-faster-data-integration/>


## <span class="section-num">6</span> Step functions {#step-functions}

-   <https://randomwits.com/blog/tutorial-cdk-aws>


### <span class="section-num">6.1</span> example created by sfn.StateMachine {#example-created-by-sfn-dot-statemachine}

```bash
{
  "StartAt": "prepareBatchJobInputTask",
  "States": {
    "prepareBatchJobInputTask": {
      "Next": "submitBatchJobs",
      "Retry": [
	{
	  "ErrorEquals": [
	    "Lambda.ServiceException",
	    "Lambda.AWSLambdaException",
	    "Lambda.SdkClientException"
	  ],
	  "IntervalSeconds": 2,
	  "MaxAttempts": 6,
	  "BackoffRate": 2
	}
      ],
      "Type": "Task",
      "ResultPath": "$.JobInput",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
	"FunctionName": "arn:aws:lambda:us-east-1:409670809604:function:HipaaAnalysisWorkflowVseq-PrepareBatchJobInputLamb-TTuXLHMdHRWv",
	"Payload.$": "$"
      }
    },
    "submitBatchJobs": {
      "Next": "runGlueTriggerFastagenerator",
      "Type": "Task",
      "InputPath": "$.JobInput",
      "Resource": "arn:aws:states:::batch:submitJob.sync",
      "Parameters": {
	"JobDefinition": "arn:aws:batch:us-east-1:409670809604:job-definition/helix-sars-klados-batch-job:3",
	"JobName": "$.JobName",
	"JobQueue": "arn:aws:batch:us-east-1:409670809604:job-queue/helix-sars-klados-batch-job-queue",
	"ArrayProperties": {
	  "Size": 1152
	},
	"ContainerOverrides": {
	  "Environment": [
	    {
	      "Name": "INPUT_S3_FOLDER",
	      "Value": "$.JobS3InputFolder"
	    },
	    {
	      "Name": "TRIM",
	      "Value": "$.JobTrimSetting"
	    }
	  ]
	},
	"RetryStrategy": {
	  "Attempts": 3
	}
      }
    },
    "runGlueTriggerFastagenerator": {
      "Next": "runGlueTriggerclassifierPart1",
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun",
      "Parameters": {
	"JobName": "research-etl-trigger-incremental-helix-seq-metrics-on-demand"
      }
    },
    "runGlueTriggerclassifierPart1": {
      "Next": "runGlueTriggerclassifierPart2",
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun",
      "Parameters": {
	"JobName": "research-etl-trigger-klados-on-demand"
      }
    },
    "runGlueTriggerclassifierPart2": {
      "End": true,
      "Type": "Task",
      "Resource": "arn:aws:states:::glue:startJobRun",
      "Parameters": {
	"JobName": "research-etl-trigger-klados-on-demand-pt2"
      }
    }
  }
}
```

```bash
    const definitionStr = `
{
  "StartAt": "prepareBatchJobInputTask",
  "States": {
    "prepareBatchJobInputTask": {
      "Next": "submitBatchJobs",
      "Type": "Task",
      "InputPath": "$",
      "ResultPath": "$.JobInput",
      "Resource": "arn:aws:states:::lambda:invoke",
      "Parameters": {
	"FunctionName": "arn:aws:lambda:us-east-1:XXX",
	"Payload.$": "$"
      }
    },
  ...
`

    new sfn.CfnStateMachine(this, 'VseqStepFunction', {
      stateMachineType: 'STANDARD',
      roleArn: 'arn:aws:iam::' + cdk.Aws.ACCOUNT_ID + ':role/' + stepFunctionRole.value,
      definitionString: definitionStr,
      tags: [
	{
	  key: 'environment',
	  value: this.namedEnv.name,
	},
      ],
    });


```


## <span class="section-num">7</span> Python library for DynamoDB {#python-library-for-dynamodb}

-   <https://highlandsolutions.com/blog/hands-on-examples-for-working-with-dynamodb-boto3-and-python>


### <span class="section-num">7.1</span> atomic counter: {#atomic-counter}

```python
# {    "siteUrl": "https://www.linuxacademy.com/",    "visits": "0"}
import boto3d = boto3.client('dynamodb')
response = dynamodb.update_item(
    TableName='siteVisits',
    Key={ siteUrl':{'S': "https://www.linuxacademy.com/"}    },
    UpdateExpression='SET visits = visits + :inc',
    ExpressionAttributeValues={ ':inc': {'N': '1'}    },
    ReturnValues="UPDATED_NEW")
print("UPDATING ITEM")
print(response)
```


## <span class="section-num">8</span> DB {#db}

-   <https://www.kdnuggets.com/2018/08/dynamodb-vs-cassandra.html>


## <span class="section-num">9</span> AWS kafka {#aws-kafka}

-   <https://aws.amazon.com/msk/>
-   <https://www.quora.com/What-is-the-difference-between-Kafka-and-Spark>


## <span class="section-num">10</span> AWS Spark {#aws-spark}

-   <https://aws.amazon.com/big-data/what-is-spark/>


## <span class="section-num">11</span> AWS redis {#aws-redis}

-   <https://aws.amazon.com/elasticache/redis/>


## <span class="section-num">12</span> My AWS resource {#my-aws-resource}

-   34.239.126.10

<!--listend-->

```bash
[fei.ni@fei-ni-C02FG3R2MD6N-SM  ~]$ cat ~/Downloads/fei-dev.pem
-----BEGIN RSA PRIVATE KEY-----
MIIEowIBAAKCAQEAqB7T5AVkUdOsm8/LkcuNTLD5w3ObOaK0Gs7+cv7kkoHGehsH
8J8G54bD564j77hWAWziRPFtISQPxppXu9BSjGs56dFdbhmwmc6+FSszq9vr/JAk
e8nXPqQPQnDpj1lA4xhuqdIZTYZo6h95cKXdN20NbAsqGqS5ZD/xk8Sbo0uHOpaH
diNZKKnI4uFSySYIiMo8tWQiIpB/f+bf79vJ+JRXWVZLOelrjjUOonzvItgR0Fr0
WNbK1uJusp8A0ut3kiKDqVJWwcS9Y/Hvn6vk5WBMgwZ24kgaHUKP0mVopH6b1Ewq
wuDzon/LtnZL/oZP+ZOvZjIc/Kf6jlHXnsxK+QIDAQABAoIBAE08PGQZBgmBkV7T
i9YjCXseIuBkD//ee5eFWOhDqYaVEDWwjWlB5c4f34hkPCY5LWniN+EseNIs2wKG
jZ+/CO1xpV2BzcZzDuraTAE1o7tkgXm6Tsh/5d7lSA1iCirM+j5aTxy9ZNp00WYd
p5DU4lhARVZJmsI6wuEHb1hPjqDppzGW0QzjArX3PhNi4YUL+9ccFERCNMw/IoCk
i3wFeAD1J+PYCZ0my7+ElUMs/8yoNe45jZLVCbpukxRlmzFYvemeq/tkJxTdxfD9
AyFtwyCJMVK7X45+JkCK1fkkGVnQwoXtbYCqaZP0Ux1hMLsnmcGIERkvAxHjgYzU
2KjBc8ECgYEA1ncK+rs5yvTRQ2JcKsgUAHb0mP2vaGYkGel30RzE0PspH5B0hQvl
Ov4CvJ9K7ud0qP9pPCLQCK+zSTTxUzqxtju/xHqjWowgmOAjPZEmGI9q7WAIACLd
SWZweN1+qp6dXvq3r960qjsEmhsVPUF2V6DKm4ei7gHYAxrMXzJ8cwUCgYEAyK4R
MKpHzZcszNWkKp+mg/qjyOwyn/gLi2ApGK7TdfWWIeg9l1YuA/SPVWGxPo9Tvg+Q
CsCQiCKOXTWjNMv9oVjdEgPuQilJt8IxOV2FubZXtx+e+c9R4QQ4X4CITo2QuyS+
lyL1NDq06w3KCABd+70ABFDVwQPNqJxzOlbvYmUCgYBmmbLl+tYOM4s9envvd6Ki
CkbAPnVBM8RHpTrODr5V4CJvWFN2Jxe2Xjj+9hIKMy7Lfs1gmKL/1Nanyi09jRHh
xbnbjHRD6E/b8zbIyHz6OPqFr3CEaCmHaPubxxNHGvTcsINaHug9nFh6RUSm9n9g
MqtbNsuKo9UsvxBQ5r1E5QKBgQCRPaojVppxKaC6/0S5tKKHkrdHi+t368YvMYGM
47sX/I6UK8mn5i+XnUC/wtzNMl6hiBHwNj5kyN3QiCl+5MTEKdSWXVHrgIZiAKIv
qohGSLpjRveARZQ1DyDdveDpOXwudgGa0So2iua12F0IPXvH3ppMhVSvRVlrVw/u
gUzwIQKBgG/Xq6VufMIlY1qkdIDvj15NtYsgnKQdKXsmIKmhiE/2dF8UGk94HC7b
H/gXrOMf1CFA9u/YqBuzY0wjkOormLiUW7jPF3QF9GoCR+XJsBDvP7M4MOP0raJx
sfeYl/DWfdK6D0dVMZasTCnCtAk9pXOaeJgoGLsAXfs3prrk4kVh
-----END RSA PRIVATE KEY-----
```
