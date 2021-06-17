---
title: "STT Apis"
date: 2021-04-21T16:00:46-07:00
draft: false
tags:
    - helix
---
# Samples
## Import samples

This endpoint import samples for "confirmatory testing".

Authentication type: HOPS token

### HTTP Request
`POST /samples/import`

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

## Return Back samples
This endpoint process a list of samples, based different op_type, it will do different work: 
op_type could be ,   `set_dna`, `return`, `place_order`

Authentication type: DUO token
### Http Request
`POST /processSamplesRequest`

### Postdata format (json)

 - op_type: `set_dna`
   - postdata format

```json
{
   "op_type": "set_dna",
   "dna_status": "sufficent|insufficent",
   "sampleIDs": [ 
       <sampleID1>,
       <sampleID2>,
       ....
   ]
}
```

 - op_type: `return`
   - postdata format

```json
{
   "op_type": "return",
   "kitIDs": [ 
       <kitID1>,
       <kitID2>,
       ....
       ]
}
```

 - op_type: `place_order`
   - postdata format

```json
{
   "op_type": "place_order",
    "samples": [ 
        {
            "kitID": <kitID>,
            "coID": <coID>,
            "testCode": <testCode>,
            "VRC": <vrc>
        }
       ....
   ]
}
```

### Response
Only HTTP status

## List Samples/Orders

### List samples
 - info_type=sample
This endpoints list samples with specified state, state can be :
 - pending
 - ordered
 - returned
If not state specified, it will return all samples 

Authentication type: DUO token
#### Http Request
`GET /info?info_type=sample&state=<state>`
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

## Update Sample DNA sample info
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

## Get Sample
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

# Orders
## Place order
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

## List orders
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

## Get Order detail
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
