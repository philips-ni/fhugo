+++
title = "AWS command line tips"
author = ["Fei Ni"]
date = 2021-07-21T14:54:47-07:00
lastmod = 2021-07-21T14:54:47-07:00
tags = ["helix"]
categories = ["helix"]
draft = false
+++

## <span class="section-num">1</span> API Gateway {#api-gateway}


### <span class="section-num">1.1</span> Get API info from API name {#get-api-info-from-api-name}

```bash
# get api_id
[fei.ni@fei-ni-C02D72XMMD6N-SM Developer-409670809604 cdk (feature/GENP-1217 *%)]$ aws apigateway get-rest-apis |grep -C2 -i SampleTracker|grep \"id\"
	    "id": "f6q7nt5z6k",
[fei.ni@fei-ni-C02D72XMMD6N-SM Developer-409670809604 cdk (feature/GENP-1217 *%)]$ aws apigateway get-resources --rest-api-id f6q7nt5z6k
{
    "items": [
	{
	    "id": "421gtq",
	    "parentId": "myxmqijazg",
	    "pathPart": "samples",
	    "path": "/samples",
	    "resourceMethods": {
		"OPTIONS": {}
	    }
	},
	{
	    "id": "9jjl41",
	    "parentId": "421gtq",
	    "pathPart": "import",
	    "path": "/samples/import",
	    "resourceMethods": {
		"OPTIONS": {},
		"POST": {}
	    }
	},
	{
	    "id": "myxmqijazg",
	    "path": "/",
	    "resourceMethods": {
		"ANY": {}
	    }
	}
    ]
}
```


## <span class="section-num">2</span> Submit batch job {#submit-batch-job}

```bash
[fei.ni@fei-ni-C02FG3R2MD6N-SM master-dev fei_work]$ cat job.json
{
    "jobName": "fei_test_r2v_new",
    "jobQueue": "arn:aws:batch:us-east-1:304674702989:job-queue/hipaa-exome-workflow-job-queue",
    "jobDefinition": "arn:aws:batch:us-east-1:304674702989:job-definition/r2v-batch-job:5",
    "containerOverrides": {
	"command": ["r2v","--platform","host","--json","s3://304674702989-hipaa-exome-workflow/test/fei/fei_test_r2v_run_cfg.json"]
    }
}

[fei.ni@fei-ni-C02FG3R2MD6N-SM master-dev fei_work]$ aws batch submit-job  --cli-input-json file://job.json
```
