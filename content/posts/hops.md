+++
title = "hops tips"
author = ["Fei Ni"]
date = 2021-04-27T18:24:21-07:00
lastmod = 2021-04-27T18:24:21-07:00
tags = ["helix"]
draft = false
+++

## <span class="section-num">1</span> create secrets between 2 services {#create-secrets-between-2-services}

-   hops secret rotate-internal-service -e test -s foo -t bar

<!--listend-->

```bash
  Yea, it’s a bit of a weird name.. but this is what it’s supposed to do under the hood.

1. Create a secret (usually something like IS-XXX)
2. hops secret add -e <environment> -s <service1> -p internal-service/<service2>/api-key/apiKey
3. hops secret add -e <environment> -s <service2> -p internal-service/<service1>/api-key/apiKey


```

and to verify with this way:

```bash
[fei.ni@fei-ni-C02D72XMMD6N-SM hipaa-staging download (feature/GENP-1139 *%)]$ hops secret rotate-internal-service -e hipaa-staging -s salesforce -t report
Secret rotated successfully.
  [fei.ni@fei-ni-C02D72XMMD6N-SM hipaa-staging download (feature/GENP-1139 *%)]$ hops secret get -e hipaa-staging -s salesforce -p internal-service/report/api-key/apiKey
  IS-NM6BKUV7QIG5SD4Z5PYLQ2KCLG2R3TOH
  [fei.ni@fei-ni-C02D72XMMD6N-SM hipaa-staging download (feature/GENP-1139 *%)]$ hops secret get -e hipaa-staging -s report -p internal-service/salesforce/api-key/apiKey
  IS-NM6BKUV7QIG5SD4Z5PYLQ2KCLG2R3TOH
```


## <span class="section-num">2</span> Use hops to access DB {#use-hops-to-access-db}

```bash
[fei.ni@fei-ni-C02D72XMMD6N-SM master myhelix]$ hops db config -f eval -e staging -s mapping
Loaded  secrets  from parameter store with subkeys:  part-1
LOCAL_PORT=$(python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')
ssh -f -o ExitOnForwardFailure=yes -L $LOCAL_PORT:ue1-staging-mapping-007-cluster.cluster-crbiutp3k1kf.us-east-1.rds.amazonaws.com:3306 fei.ni@172.19.69.18 sleep 60 && \
MYSQL_PWD='2vNv3hkWqaqwqb' mysql mapping --host=127.0.0.1 --port=${LOCAL_PORT} --user='mapping-service'

Notice: to replace host with the aws hostname, and replace the port with 3306

[fei.ni@fei-ni-C02D72XMMD6N-SM master myhelix]$ MYSQL_PWD='2vNv3hkWqaqwqb' mysql mapping --host=ue1-staging-mapping-007-cluster.cluster-crbiutp3k1kf.us-east-1.rds.amazonaws.com --port=3306 --user='mapping-service'
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 136276
Server version: 5.6.10 MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql> \
```


## <span class="section-num">3</span> DB tips {#db-tips}

| Action            | mysql Command          | postgresql Command |
|-------------------|------------------------|--------------------|
| list dbs          | show databases         |                    |
| switch db         | use <db\_name>         |                    |
| list tables       | show tables            | \dt                |
| show table schema | describe <table\_name> | \d <table\_name>   |


## <span class="section-num">4</span> Links {#links}

-   <https://myhelix.atlassian.net/wiki/spaces/ENG/pages/777420817/Managing+Serialized+Secrets+in+Parameter+Store>
