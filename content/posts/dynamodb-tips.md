+++
title = "DynamoDB tips"
author = ["Fei Ni"]
date = 2021-06-28T09:07:15-07:00
lastmod = 2021-06-28T09:07:15-07:00
tags = ["helix"]
categories = ["helix"]
draft = false
+++

## <span class="section-num">1</span> Paginating {#paginating}

-   <https://www.matthewsessions.com/blog/paginating-dynamo-query-scan/>
-   <https://www.talentica.com/blogs/dynamo-db-pagination/>


## <span class="section-num">2</span> common commands {#common-commands}

-   <https://dynobase.dev/dynamodb-cli-query-examples/#scan>


## <span class="section-num">3</span> Clear a table {#clear-a-table}

```bash
[fei.ni@fei-ni-C02FG3R2MD6N-SM hippa-staging sample-tracker (release/0.1.0 %)]$ cat del_all.sh
tableName=$1
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
