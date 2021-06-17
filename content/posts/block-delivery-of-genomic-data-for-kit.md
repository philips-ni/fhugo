+++
title = "How to block the delivery of genomic data for a kit"
author = ["Fei Ni"]
date = 2021-05-14T17:05:18-07:00
lastmod = 2021-05-14T17:05:18-07:00
tags = ["helix"]
categories = ["helix"]
draft = false
+++

## <span class="section-num">1</span> Overview {#overview}


### <span class="section-num">1.1</span> Input {#input}

A list of kitID


### <span class="section-num">1.2</span> Output {#output}

-   A Google doc
-   BSSH meta updated
-   DB updated(sampleCallSets table in mapping service)


## <span class="section-num">2</span> Steps {#steps}


### <span class="section-num">2.1</span> Generate sampleID list by kitID list by querying mapping service {#generate-sampleid-list-by-kitid-list-by-querying-mapping-service}

Need connect AWS VPN to Master-oncall

```bash
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall feiws]$ cat kits |python3 gen_sql.py >samples.sql
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall feiws]$ MYSQL_PWD='L3vNFRHXAvjme9' mysql mapping --host=ue1-production-rds-mapping-002.cluster-crbiutp3k1kf.us-east-1.rds.amazonaws.com --port=3306 --user='mapping-service' <samples.sql >out
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall feiws]$ cat out
sampleId	kitId
SA-XERX-C96EE	BRLWLAE708
SA-F22E-68YJE	CCVWLAB587
SA-E74N-4D5KN	DWLWLAE320
SA-RU56-FQE5H	HTZWLAE402
SA-MTN2-BJZ6C	HZIWLAE015
SA-CMY2-UECSQ	NJGWLAE851
SA-MUKD-NJSUG	NQOVEAB539
SA-V56V-88452	NYOWLAC335
SA-UJCP-BFVZR	OBKVKAI487
SA-H4F2-VAS9Q	PBKWLAB298
SA-6XSE-U24MR	PPIVKAI208
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall feiws]$ cat out |cut -f1|sed -e '1d' >samples
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall feiws]$ cat samples
SA-XERX-C96EE
SA-F22E-68YJE
SA-E74N-4D5KN
SA-RU56-FQE5H
SA-MTN2-BJZ6C
SA-CMY2-UECSQ
SA-MUKD-NJSUG
SA-V56V-88452
SA-UJCP-BFVZR
SA-H4F2-VAS9Q
SA-6XSE-U24MR
```


### <span class="section-num">2.2</span> Generate bioSampleIDs by sampleIDs by querying ODB {#generate-biosampleids-by-sampleids-by-querying-odb}

Need connect Global connect VPN

```bash
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall feiws]$ cat samples |python3 gen_sql3.py > in_odb.sql
[fei.ni@fei-ni-C02D72XMMD6N-SM Master-oncall feiws]$ psql -h odb.helix.com -p 5439 -U opsread odb <in_odb.sql | sed -e '1,2d' |grep -v rows|awk '{print $1}' >bioSamples
```


### <span class="section-num">2.3</span> Cancel samples in Bssh {#cancel-samples-in-bssh}

```bash
$ cat disable_sample_in_bssh.sh
basespace_prod_api_token=$(cat production_token )
bioSampleID=$1
if [[ $bioSampleID != "" ]];then
    curl -X POST "https://api.basespace.illumina.com/v2/biosamples/${bioSampleID}/properties" \
         -H 'Content-Type: application/json' \
         -H "Authorization: Bearer ${basespace_prod_api_token}" \
         -d '{
             "Properties": [
                  {
                      "Type": "string",
                      "Name": "Metadata.Disabled",
                      "Description": "Disabled",
                      "Content": "true"
                  }
             ]
           }'
fi
$ for i in $(cat bioSamples);do sh -x disable_sample_in_bssh.sh $i;done
```


### <span class="section-num">2.4</span> Record the plan-to-del info then delete them {#record-the-plan-to-del-info-then-delete-them}

```bash
$ cat kits |python3 gen_sql2.py >store_and_del_mapping.sql
select *
from sampleCallSets
where sampleId in (select sampleId from userSamples where kitId in (
  "HTZWLAE402",
  "NQOVEAB539",
  "NYOWLAC335",
  "NJGWLAE851",
  "HZIWLAE015",
  "CCVWLAB587",
  "PPIVKAI208",
  "DWLWLAE320",
  "PBKWLAB298",
  "OBKVKAI487",
  "BRLWLAE708"
));

delete
from sampleCallSets
where sampleId in (select sampleId from userSamples where kitId in (
  "HTZWLAE402",
  "NQOVEAB539",
  "NYOWLAC335",
  "NJGWLAE851",
  "HZIWLAE015",
  "CCVWLAB587",
  "PPIVKAI208",
  "DWLWLAE320",
  "PBKWLAB298",
  "OBKVKAI487",
  "BRLWLAE708"
));
$ MYSQL_PWD='L3vNFRHXAvjme9' mysql mapping --host=ue1-production-rds-mapping-002.cluster-crbiutp3k1kf.us-east-1.rds.amazonaws.com --port=3306 --user='mapping-service' <store_and_del_mapping.sql
sampleId	callSetId	createdAt	pipelineVersion	reanalysisRequestedAt	analysisId
SA-MUKD-NJSUG	WBCQQYZH6VETX9YMW9DH	2020-03-17 01:37:26.622434	NULL	NULL	AN-JZE32YCTXQFSJ5X2NLF5JHXKQXHMK7ZK
SA-V56V-88452	Y9GGR4GHRNWQB64YA3RW	2021-02-24 04:32:45.550194	NULL	NULL	AN-FBMT6YKCKZEWOSN6NWDJIWGREZ2BCV6J

# Second run should return nothing to prove they are deleted successfully
$ MYSQL_PWD='L3vNFRHXAvjme9' mysql mapping --host=ue1-production-rds-mapping-002.cluster-crbiutp3k1kf.us-east-1.rds.amazonaws.com --port=3306 --user='mapping-service' <store_and_del_mapping.sql


```


### <span class="section-num">2.5</span> Create google doc {#create-google-doc}

-   under <https://drive.google.com/drive/folders/1yqHMjkrgK86Lqqm2c-2jvDNjyj6w0SLq>


## <span class="section-num">3</span> Related links {#related-links}

-   <https://myhelix.atlassian.net/wiki/spaces/DLS/pages/2375155753/How+to+block+the+delivery+of+genomic+data+for+a+kit>
