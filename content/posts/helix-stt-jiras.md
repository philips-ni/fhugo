---
title: "Helix STT Jiras"
date: 2021-04-22T23:44:47-07:00
draft: false
tags:
  - helix
---

# [STT] Init repo & CDK
Check https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2277802167/STT+--+Sample+Tracker+Tool for architecture overview


# Implement endpoint to import samples
Check https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2277802167/STT+--+Sample+Tracker+Tool for architecture overview

This endpoint import samples for "confirmatory testing".

Authentication type: HOPS token

### HTTP Request
`POST /samples`

### Postdata format (json)

```json
[ 
    {
        "kitID": "XXX",
        "pacID": "XXX",
        "testcode": "XXX",
        "vrc": "xxx"
    },
    ...
]

```

### Response
Only HTTP status

# Implement endpoint to return back samples
Check https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2277802167/STT+--+Sample+Tracker+Tool for architecture overview

This endpoint send a list of kitID back to my health workflow

Authentication type: DUO token
### Http Request
`POST /returnSamplesRequest`

### Postdata format (json)

```json
[ 
    <kitID1>,
    <kitID2>,
    ....
]
```

### Response
Only HTTP status

# Implement endpoint to list samples
Check https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2277802167/STT+--+Sample+Tracker+Tool for architecture overview

This endpoints list samples with specified state, state can be :
 - pending
 - ordered
 - returned
If no state specified, it will return all samples

Authentication type: DUO token
### Http Request
`GET /samples?state=<state>`
### Query String
 - state
### Response (json)
```
[ 
    {
        "sampleID": "XXX",
        "pacID": "XXX",
        "kitID": "XXX",
        "coID": "XXX",
        "testcode": "XXX",
        "vrc": "xxx",
        "state": "xxx",
        "sufficentDNA": "xxx",
        "importeddBy": "xxx",
        "processedBy": "xxx",
        "processedAt": "xxx"
    },
    ...
]

```

# Implement endpoint to update sample DNA sample info
Check https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2277802167/STT+--+Sample+Tracker+Tool for architecture overview

This endpoint update "sufficentDNA" for specified sample

Authentication type: DUO token

### Http Request
`PUT /sample/<sampleID>`

### Postdata format (json)
```json
{
   "sufficentDNA": "YES|NO"
}
```
### Response
Only HTTP status

# Implement endpoints to get sample detail by coID and PEID
Check https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2277802167/STT+--+Sample+Tracker+Tool for architecture overview

This endpoint return sample detail by `coID` and `PEID`

Authentication type: HOPS token
### Http Request
`GET /sample?coID=<coID>&PEID=<PEID>`

### Postdata format (json)
```json
{
    "sampleID": "XXX",
    "pacID": "XXX",
    "kitID": "XXX",
    "coID": "XXX",
    "testcode": "XXX",
    "vrc": "xxx",
    "state": "xxx",
    "sufficentDNA": "xxx",
    "importeddBy": "xxx",
    "processedBy": "xxx",
    "processedAt": "xxx"
}
```
### Response
Only HTTP status



# Implement endpoint to place order
Check https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2277802167/STT+--+Sample+Tracker+Tool for architecture overview

This endpoint places order for a list of samples

Authentication type: DUO token
### Http Request
`POST /orders`

### Postdata format (json)
```json
[ 
    <sampleID1>,
    <sampleID2>,
    ....
]
```


### Response
#### Response format (json)
```json
{ 
  "orderID" : xxx,
  "samples": 
    [ 
        {
            "sampleID" : "xxx",
            "PEID: "xxx
        },
    ...
    ]
}
```

# Implement endpoint to list orders
Check https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2277802167/STT+--+Sample+Tracker+Tool for architecture overview

This endpoint lists all orders

Authentication type: DUO token
### Http Request
`GET /orders`
### Response
#### Response format (json)
```json
[ 
  {
    "orderID" : xxx,
    "samples": 
        [ 
            "sampleID1",
            "sampleID2"
        ],
    "createdBy": "xxx",
    "createdAt: "xxx",
    "trackingNum" : "xxx"
  }
]
```

# Implement endpoint to get order detail
Check https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2277802167/STT+--+Sample+Tracker+Tool for architecture overview

This endpoint return detail of specified order

Authentication type: DUO token
### Http Request
`GET /order/<orderID>`
### Response
#### Response format (json)
```json
{ 
    "orderID" : xxx,
    "samples": 
        [ 
            "sampleID": "xxx",
            "PEID": "xxx",
            "coID": "xxx",
            "testcode", "xxx",
            "vrc": "xxx"
        ],
    "createdBy": "xxx",
    "createdAt: "xxx",
    "trackingNum" : "xxx"
  }
}
```


## Update order tracking number
This endpoint update tracking number for specified order

Authentication type: DUO token
### Http Request
`PUT /order/<orderID>`
### Postdata format (json)
```json
{
  "trackingNum": "xxx"
}
```
### Response
Only HTTP status


# Implement API to query sample location API in lab library
Check https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2277802167/STT+--+Sample+Tracker+Tool for architecture overview.

see https://myhelix.atlassian.net/browse/GENP-1203 for the detail about the sql to get location info by querying LIMS replica
# Implement API to create Perkin Elmer order

Check https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2277802167/STT+--+Sample+Tracker+Tool for architecture overview.

This API could be provided from a golang library, we can consider to create new git repo for it

## input
 1. coID
 2. sampleID
 3. pacID
## output
 1. Error (nil means succeed)
 2. peID

 Please refer https://github.com/myhelix/myhealth-workflow/blob/master/clients/pelims/pelims.go
