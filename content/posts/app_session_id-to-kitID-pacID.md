+++
title = "app_session_id to kitID and pacID"
author = ["Fei Ni"]
date = 2021-05-18T13:09:32-07:00
lastmod = 2021-05-18T13:09:32-07:00
tags = ["helix"]
categories = ["helix"]
draft = false
+++

## <span class="section-num">1</span> app\_session\_id to KitID {#app-session-id-to-kitid}


### <span class="section-num">1.1</span> app\_session\_id to sampleID {#app-session-id-to-sampleid}


#### <span class="section-num">1.1.1</span> accessing ODB {#accessing-odb}

```bash
# Beforeing running this please use GlobalProtect VPN
# password can be found from https://helix-engineering.1password.com/vaults/gxhrwag245jkcrq7dvulaivmnq/allitems/2jte2zc3knd4pboslqbtk2o7y4
$ psql -h odb.helix.com -p 5439 -U opsread odb
```


#### <span class="section-num">1.1.2</span> Run Sql {#run-sql}

```bash
odb=> select app_session_id, sample_id from samplemetadata_analysis_stream where app_session_id in ('397814418', '342203880', '383018636', '381759393');
 app_session_id |   sample_id
----------------+---------------
 381759393      | SA-UJUB-ZJB3W
 381759393      | SA-UJUB-ZJB3W
 397814418      | SA-4JUG-KZYW4
 397814418      | SA-4JUG-KZYW4
 397814418      | SA-4JUG-KZYW4
 342203880      | SA-CYA2-JKZGY
 342203880      | SA-CYA2-JKZGY
 342203880      | SA-CYA2-JKZGY
 342203880      | SA-CYA2-JKZGY
 381759393      | SA-UJUB-ZJB3W
 381759393      | SA-UJUB-ZJB3W
 383018636      | SA-TRZM-QERBH
 381759393      | SA-UJUB-ZJB3W
 383018636      | SA-TRZM-QERBH
 397814418      | SA-4JUG-KZYW4
 342203880      | SA-CYA2-JKZGY
 342203880      | SA-CYA2-JKZGY
 342203880      | SA-CYA2-JKZGY
 342203880      | SA-CYA2-JKZGY
 381759393      | SA-UJUB-ZJB3W
 381759393      | SA-UJUB-ZJB3W
 383018636      | SA-TRZM-QERBH
 383018636      | SA-TRZM-QERBH
 383018636      | SA-TRZM-QERBH
 383018636      | SA-TRZM-QERBH
 383018636      | SA-TRZM-QERBH
 381759393      | SA-UJUB-ZJB3W
 383018636      | SA-TRZM-QERBH
 397814418      | SA-4JUG-KZYW4
 397814418      | SA-4JUG-KZYW4
 342203880      | SA-CYA2-JKZGY
 342203880      | SA-CYA2-JKZGY
 381759393      | SA-UJUB-ZJB3W
 381759393      | SA-UJUB-ZJB3W
 383018636      | SA-TRZM-QERBH
 383018636      | SA-TRZM-QERBH
 397814418      | SA-4JUG-KZYW4
 397814418      | SA-4JUG-KZYW4
 397814418      | SA-4JUG-KZYW4
(39 rows)

[fei.ni@fei-ni-C02D72XMMD6N-SM Hippa-platform-development PA-1172]$ cat raw_mapping.txt |grep SA|sort|uniq
 app_session_id | sample_id
------------------------------------
 342203880      | SA-CYA2-JKZGY
 381759393      | SA-UJUB-ZJB3W
 383018636      | SA-TRZM-QERBH
 397814418      | SA-4JUG-KZYW4

$ cat raw_mapping.txt |grep SA|sort|uniq|cut -d'|' -f2 |awk '{print $1}' >sampleIDs
```


### <span class="section-num">1.2</span> sampleID to kitID {#sampleid-to-kitid}

-   switch to use aws profile Master-oncall
-   use AWS production VPN

<!--listend-->

```bash
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$ cat in.sql
select sampleId, kitId from userSamples where sampleId in (
  "SA-CYA2-JKZGY",
  "SA-UJUB-ZJB3W",
  "SA-TRZM-QERBH",
  "SA-4JUG-KZYW4"
);

[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$ MYSQL_PWD='L3vNFRHXAvjme9' mysql mapping --host=ue1-production-rds-mapping-002.cluster-crbiutp3k1kf.us-east-1.rds.amazonaws.com --port=3306 --user='mapping-service' <in.sql >out
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$ cat out
sampleId	kitId
SA-4JUG-KZYW4	MMNWLAF348
SA-CYA2-JKZGY	DZZVKAS394
SA-TRZM-QERBH	FVZWLAE133
SA-UJUB-ZJB3W	LNRWLAE582
```


## <span class="section-num">2</span> app\_session\_id to pacID {#app-session-id-to-pacid}


### <span class="section-num">2.1</span> app\_session\_id to sampleID {#app-session-id-to-sampleid}

See above


### <span class="section-num">2.2</span> sampleID to userID {#sampleid-to-userid}

```bash
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$ cat in.sql
select sampleId, kitId, userId from userSamples where sampleId in (
  "SA-CYA2-JKZGY",
  "SA-UJUB-ZJB3W",
  "SA-TRZM-QERBH",
  "SA-4JUG-KZYW4"
);

[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$ MYSQL_PWD='L3vNFRHXAvjme9' mysql mapping --host=ue1-production-rds-mapping-002.cluster-crbiutp3k1kf.us-east-1.rds.amazonaws.com --port=3306 --user='mapping-service' <in.sql >out
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$ cat out
sampleId	kitId	userId
SA-4JUG-KZYW4	MMNWLAF348	US-442N-G5B7D
SA-CYA2-JKZGY	DZZVKAS394	US-ZVZS-2TUAK
SA-TRZM-QERBH	FVZWLAE133	US-ZNZU-8CFWB
SA-UJUB-ZJB3W	LNRWLAE582	US-V3GV-XBSYU
```


### <span class="section-num">2.3</span> Get appID {#get-appid}

please refer to <https://github.com/myhelix/hmapi/blob/master/models/catalog/json/items.json> for appID from appName

the appID for mayo tapestry research is AP-WAJ7RB36A55MCXGQHSJ7GWZKQZSQGFZO


### <span class="section-num">2.4</span> "userID, appID" to pacID {#userid-appid-to-pacid}


#### <span class="section-num">2.4.1</span> access customer DB {#access-customer-db}

```bash
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$ hops db list -e production
ListOrGetSecrets failed: invalid secrets. Both secrets/all and secrets/part-XXX present
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$ hops db config -f eval -e production -s customer
Loaded  secrets  from parameter store with subkeys:  part-1, part-2

#    WARNING WARNING WARNING WARNING WARNING
#    This is a production database. Please be careful!

LOCAL_PORT=$(python -c 'import socket; s=socket.socket(); s.bind(("", 0)); print(s.getsockname()[1]); s.close()')
ssh -f -o ExitOnForwardFailure=yes -L $LOCAL_PORT:production-customer.cluster-crbiutp3k1kf.us-east-1.rds.amazonaws.com:3306 fei.ni@172.20.132.123 sleep 60 && \
MYSQL_PWD='jHrPrWCMGtFB9pwHChnD' mysql customer --host=127.0.0.1 --port=${LOCAL_PORT} --user='customer-service'
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$ MYSQL_PWD='jHrPrWCMGtFB9pwHChnD' mysql customer --host=production-customer.cluster-crbiutp3k1kf.us-east-1.rds.amazonaws.com --port=3306 --user='customer-service'
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Welcome to the MySQL monitor.  Commands end with ; or \g.
Your MySQL connection id is 342
Server version: 5.7.12 MySQL Community Server (GPL)

Copyright (c) 2000, 2021, Oracle and/or its affiliates.

Oracle is a registered trademark of Oracle Corporation and/or its
affiliates. Other names may be trademarks of their respective
owners.

Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.

mysql>
```


#### <span class="section-num">2.4.2</span> Run SQL {#run-sql}

```bash
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$ cat in.sql
select appId, userId, partnerAppCustomerId from userApps where appID='AP-WAJ7RB36A55MCXGQHSJ7GWZKQZSQGFZO' and userID in (
  "US-442N-G5B7D",
  "US-ZVZS-2TUAK",
  "US-ZNZU-8CFWB",
  "US-V3GV-XBSYU"
);
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$ MYSQL_PWD='jHrPrWCMGtFB9pwHChnD' mysql customer --host=production-customer.cluster-crbiutp3k1kf.us-east-1.rds.amazonaws.com --port=3306 --user='customer-service' <in.sql >out
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall PA-1172]$ cat out
appId	userId	partnerAppCustomerId
AP-WAJ7RB36A55MCXGQHSJ7GWZKQZSQGFZO	US-442N-G5B7D	PC-AVG5UMEPKZOE5QDJMQXTACNF43ZMYH62
AP-WAJ7RB36A55MCXGQHSJ7GWZKQZSQGFZO	US-V3GV-XBSYU	PC-FON7AKSRHHAT4XC5HPV7MAQXI422YHXB
AP-WAJ7RB36A55MCXGQHSJ7GWZKQZSQGFZO	US-ZNZU-8CFWB	PC-VF4YONCJCV6BDH6474KMKH333NXWMHF7
AP-WAJ7RB36A55MCXGQHSJ7GWZKQZSQGFZO	US-ZVZS-2TUAK	PC-PAYT3BT7N6SRB7PFJYC6ZHVW26OA44D3
```


## <span class="section-num">3</span> Final report {#final-report}

| AppSessionID | chr:pos:ref:alt   | sampleID      | userID        | KitID      | pacID                               |
|--------------|-------------------|---------------|---------------|------------|-------------------------------------|
| 397814418    | chrX:12886996:G:C | SA-4JUG-KZYW4 | US-442N-G5B7D | MMNWLAF348 | PC-AVG5UMEPKZOE5QDJMQXTACNF43ZMYH62 |
| 342203880    | chrX:12887841:T:G | SA-CYA2-JKZGY | US-ZVZS-2TUAK | DZZVKAS394 | PC-PAYT3BT7N6SRB7PFJYC6ZHVW26OA44D3 |
| 383018636    | chrX:12888155:C:T | SA-TRZM-QERBH | US-ZNZU-8CFWB | FVZWLAE133 | PC-VF4YONCJCV6BDH6474KMKH333NXWMHF7 |
| 381759393    | chrX:12888156:G:A | SA-UJUB-ZJB3W | US-V3GV-XBSYU | LNRWLAE582 | PC-FON7AKSRHHAT4XC5HPV7MAQXI422YHXB |

| AppSessionID | chr:pos:ref:alt   | KitID      | pacID                               |
|--------------|-------------------|------------|-------------------------------------|
| 397814418    | chrX:12886996:G:C | MMNWLAF348 | PC-AVG5UMEPKZOE5QDJMQXTACNF43ZMYH62 |
| 342203880    | chrX:12887841:T:G | DZZVKAS394 | PC-PAYT3BT7N6SRB7PFJYC6ZHVW26OA44D3 |
| 383018636    | chrX:12888155:C:T | FVZWLAE133 | PC-VF4YONCJCV6BDH6474KMKH333NXWMHF7 |
| 381759393    | chrX:12888156:G:A | LNRWLAE582 | PC-FON7AKSRHHAT4XC5HPV7MAQXI422YHXB |