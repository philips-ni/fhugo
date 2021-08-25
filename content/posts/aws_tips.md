+++
title = "AWS tips"
author = ["Fei Ni"]
date = 2021-07-20T09:53:39-07:00
lastmod = 2021-07-20T09:53:39-07:00
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


## <span class="section-num">5</span> Python library for DynamoDB {#python-library-for-dynamodb}

-   <https://highlandsolutions.com/blog/hands-on-examples-for-working-with-dynamodb-boto3-and-python>
