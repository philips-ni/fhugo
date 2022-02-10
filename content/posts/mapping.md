+++
title = "Helix Mapping of those entities"
author = ["Fei Ni"]
date = 2022-01-19T14:42:47-08:00
lastmod = 2022-01-19T14:42:47-08:00
tags = ["helix"]
draft = false
+++

## <span class="section-num">1</span> userSamples table {#usersamples-table}

It defines the  mapping between user and sample.

```sql
CREATE TABLE IF NOT EXISTS userSamples (
    kitId      VARCHAR(39)           NOT NULL,
    userId     VARCHAR(39)           NOT NULL,
    sampleId   VARCHAR(39)           NOT NULL,
    createdAt  TIMESTAMP(6)          NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY(kitId)
);

```

A new entry will be added while user calling POST _userSamples ,  the input would be a list of kitId, accordingly , sampleId will be generated automatically_


## <span class="section-num">2</span> sampleCallSets {#samplecallsets}

A sample callset maps a user sample to an analysis object. The analysis object is Helix's internal way of tracking the sample as it runs through our workflows, and keeps track of all the analyses/interpretations that have been run on

```sql

CREATE TABLE IF NOT EXISTS sampleCallSets (
    sampleId   VARCHAR(39)           NOT NULL,
    callSetId  VARCHAR(39)           NOT NULL,
    createdAt  TIMESTAMP(6)          NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY(callSetId)
)

```


## <span class="section-num">3</span> appAnalysisMinVersions {#appanalysisminversions}

It defines the mapping between appID, version/min\_version to analysistype

Required analysistype can be identified by appID

```sql
CREATE TABLE IF NOT EXISTS appAnalysisMinVersions (
    appId         VARCHAR(39)           NOT NULL,
    analysisType  VARCHAR(20)           NOT NULL,
    version       INT                   NOT NULL,
    minVersion    VARCHAR(255)          NOT NULL,
    createdAt     TIMESTAMP(6)          NOT NULL DEFAULT CURRENT_TIMESTAMP(6),
    PRIMARY KEY(appId, analysisType, version)
);
```

```golang
// GetMaxMinVersions returns the maximum of all min version requirements for the given apps.
// For those analysis types that are config based, it returns all min version requirements
// ctx is the context logger
// appIds is the list of app ids
func GetMaxMinVersions(ctx log.ContextLogger, appIds []string) ([]AppAnalysisMinVersion, error) {
 ...
```


## <span class="section-num">4</span> DB info {#db-info}

```bash
mysql> select * from appAnalysisMinVersions
-> ;
 +-------------------------------------+---------------------+---------+------------+----------------------------+
 | appId                               | analysisType        | version | minVersion | createdAt                  |
 +-------------------------------------+---------------------+---------+------------+----------------------------+
 | AP-3D6AZAJ2REWW5D24NGKS5HGU34X5ARYF | r2v                 |       1 | 2.3.0      | 2017-02-08 22:53:37.758554 |
 | AP-3I7GZ6AVDTPROGI2Q6TKACVIYTMOA4A2 | r2v                 |       1 | 2.3.0      | 2017-05-04 04:22:17.949137 |
 | AP-3I7GZ6AVDTPROGI2Q6TKACVIYTMOA4A2 | r2v                 |       2 | 2.3.0      | 2017-06-07 22:07:31.903388 |
 | AP-3I7GZ6AVDTPROGI2Q6TKACVIYTMOA4A2 | r2v                 |       3 | 2.3.0      | 2017-06-07 22:13:00.360705 |
 | AP-3I7GZ6AVDTPROGI2Q6TKACVIYTMOA4A2 | r2v                 |       4 | 2.3.0      | 2017-06-26 23:17:40.937092 |
 | AP-3I7GZ6AVDTPROGI2Q6TKACVIYTMOA4A2 | r2v                 |       5 | 2.3.0      | 2017-06-30 20:28:26.727582 |
 | AP-4PJQZ2CCDEN4X57TVRAGAD27RT5BA3WH | SimpleTraits        |       1 | 6.0.15     | 2019-04-09 18:50:16.688845 |
 | AP-4PJQZ2CCDEN4X57TVRAGAD27RT5BA3WH | u2v                 |       1 | 0.0.1      | 2019-04-15 18:52:48.467211 |
 | AP-4QMZA6ZSXJBTGCXTYVNWUPJDU3X2W7IO | r2v                 |       1 | 2.3.0      | 2017-08-15 23:46:59.044287 |
 | AP-4QMZA6ZSXJBTGCXTYVNWUPJDU3X2W7IO | r2v                 |       2 | 2.3.0      | 2017-09-19 19:54:24.915295 |
 | AP-4QMZA6ZSXJBTGCXTYVNWUPJDU3X2W7IO | r2v                 |       3 | 2.3.0      | 2017-11-17 19:12:34.546720 |
	...
```


## <span class="section-num">5</span> ID prefix {#id-prefix}

```bash

var (
	ANALYSIS                  = newUuidPrefix("AN", strongKeyMethod)
	ANALYSIS_GROUP            = newUuidPrefix("AG", strongKeyMethod)
	APP                       = newUuidPrefix("AP", strongKeyMethod)
	BATCH_ID                  = newUuidPrefix("BA", strongKeyMethod)
	BUNDLE_ID                 = newUuidPrefix("BU", strongKeyMethod)
	CLIENT                    = newUuidPrefix("CL", strongKeyMethod)
	CLIENT_SECRET             = newUuidPrefix("CS", strongKeyMethod)
	CONFIRM_EMAIL             = newUuidPrefix("CE", strongKeyMethod)
	GENERIC_SECRET            = newUuidPrefix("SC", strongKeyMethod)
	GENOMIC_UPLOAD            = newUuidPrefix("GU", humanReadableMethod)
	INTERNAL_SERVICE          = newUuidPrefix("IS", strongKeyMethod)
	INTERPRETATION_COLLECTION = newUuidPrefix("IC", strongKeyMethod)
	METRIC_COLLECTION         = newUuidPrefix("MC", strongKeyMethod)
	PARTNER                   = newUuidPrefix("PA", strongKeyMethod)
	PAC                       = newUuidPrefix("PC", strongKeyMethod)
	PASSWORD_RESET            = newUuidPrefix("PR", strongKeyMethod)
	REFRESH_TOKEN             = newUuidPrefix("RF", strongKeyMethod)
	SAMPLE                    = newUuidPrefix("SA", humanReadableMethod)
	STATE_MACHINE             = newUuidPrefix("SM", strongKeyMethod)
	TEST_SAMPLE               = newUuidPrefix("ST", looselyHumanReadableMethod)
	TWO_FACTOR_AUTH_TOKEN     = newUuidPrefix("FA", humanReadableMethod)
	USER                      = newUuidPrefix("US", humanReadableMethod)
	VAULT_APPID               = newUuidPrefix("VA", strongKeyMethod)
	VAULT_USERID              = newUuidPrefix("VU", strongKeyMethod)
)
```


## <span class="section-num">6</span> Find sampleId/kitId mapping in production/staging {#find-sampleid-kitid-mapping-in-production-staging}

-   connect to AWS VPN (<https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2063597598/AWS+VPN>)
-   connect to mapping DB to run the query

    ```bash
    # hops db config -f eval -e production -s mapping
    MYSQL_PWD='L3vNFRHXAvjme9' mysql mapping --host=ue1-production-rds-mapping-002.cluster-crbiutp3k1kf.us-east-1.rds.amazonaws.com --port=3306 --user='mapping-service' <in >out
    MYSQL_PWD='2vNv3hkWqaqwqb' mysql mapping --host=ue1-staging-mapping-007-cluster.cluster-crbiutp3k1kf.us-east-1.rds.amazonaws.com --port=3306 --user='mapping-service' <in >out
    ```

A help script to convert a sampleID list to sql input file

```python
import sys

SQL_TPL = """select sampleId, kitId from userSamples where sampleId in (
{});
"""


def main():
    lines = sys.stdin.readlines()
    content = ""
    for idx, line in enumerate(lines):
	if idx != len(lines) - 1:
	    content += '  "{}",\n'.format(line.rstrip())
	else:
	    content += '  "{}"\n'.format(line.rstrip())
    output = SQL_TPL.format(content)
    print(output)


if __name__ == "__main__":
    sys.exit(main())
```


## <span class="section-num">7</span> BatchID to step functions execution ARN {#batchid-to-step-functions-execution-arn}

Searching ODB

```bash
[fei.ni@fei-ni-C02FG3R2MD6N-SM master-oncall sample_biosample (b_dev_add_samplesheet_util *%)]$ psql -h odb.helix.com -p 5439 -U opsread odb
Password for user opsread:
psql (14.1, server 8.0.2)
SSL connection (protocol: TLSv1.2, cipher: ECDHE-RSA-AES256-GCM-SHA384, bits: 256, compression: off)
Type "help" for help.

odb=> SELECT json_executionarn FROM sm_batch_current WHERE id = 'BA-4TKYFURG2YBDQNJXE4GB2HRBWGEXINDA';
							   json_executionarn
----------------------------------------------------------------------------------------------------------------------------------------
 arn:aws:states:us-east-1:820411415250:execution:analysis-workflow-production-cnv-state-machine-dp:da67eedc-46f3-40ea-b0a8-829f6ede3ecc
(1 row)
```


## <span class="section-num">8</span> Links {#links}

-   <https://myhelix.atlassian.net/wiki/spaces/ENG/pages/1029439860/Genomic+Data+Service+Process+System+Overview#Sample-Callsets>
