---
title: "Jira Cli"
date: 2021-04-22T23:31:02-07:00
draft: false
tags:
  - tool

---

### curl command to create Jira issue
```bash
curl -v --request POST \
  --url 'https://<company>.atlassian.net/rest/api/3/issue' \
  --user 'fei.ni@helix.com:<JIRA_API_TOKEN>' \
  --header 'Accept: application/json' \
  --header 'Content-Type: application/json' \
  -d @jira.json
```

```bash
[fei.ni@fei-ni-C02D72XMMD6N-SM  go-jira]$ cat jira.json
{
  "fields":{
    "project":{
      "key": "GENP"
    },
    "summary":  "[STT]Init repo & CDK",
    "description": {
      "type": "doc",
      "version": 1,
      "content": [
        {
          "type": "paragraph",
          "content": [
            {
              "type": "text",
              "text": "Init repo & CDK"
            }
          ]
        }
      ]
    },
    "issuetype": {"name": "Story"}
  }
}
```

### Links
 - https://community.developer.atlassian.com/t/post-html-issue-description-with-jira-rest-api-v3/38482

