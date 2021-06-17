+++
title = "Interview with Ravali"
author = ["Fei Ni"]
date = 2021-06-02T20:06:11-07:00
lastmod = 2021-06-02T20:06:11-07:00
tags = ["helix"]
categories = ["helix"]
draft = false
+++

## <span class="section-num">1</span> Basic Info {#basic-info}

| Candidate Name | Kumar Subramanian    |
|----------------|----------------------|
| Job Level      | Senior               |
| Type           | Tech phone screening |
| Date           | 06/02/2021           |

Highlight:

-   20+ years experience


## <span class="section-num">2</span> timeline {#timeline}

| Time           | activity                                                                                     |
|----------------|----------------------------------------------------------------------------------------------|
| 16:00          | Interview started                                                                            |
| 16:10          | Switch to coding challenge, had some trouble to open coderpad, that's why it's a little late |
| 16:13          | Start coding                                                                                 |
| 16:30 to 16:37 | Stuck at rule 5                                                                              |
| 16:42          | Start to compile and run before implementing rule 6 and 7                                    |
| 17:09          | Stop the session, still not be able to resolve the compilation error                         |


## <span class="section-num">3</span> General notes {#general-notes}

-   Start quickly without asking questions
-   Deal with each rule one by one, start implementing without having overall understanding of the requirement
-   Using functional style Java, but not very familiar with it, Took a long time to resolve syntax error, and failed to resolve it at the end
-   Didn't get time to run test with her implementation


## <span class="section-num">4</span> More {#more}

```sql
SELECT
   s.name AS SampleName,
   c.name AS PlateName,
   cp.wellxposition,
   cp.wellyposition
FROM
   lims_sample s
INNER JOIN lims_artifact_sample_map asm
   ON asm.processid = s.processid
INNER JOIN lims_artifact a
   ON asm.artifactid = a.artifactid
INNER JOIN lims_containerplacement cp
   ON cp.processartifactid = a.artifactid
INNER JOIN lims_container c
   ON (
   c.containerid = cp.containerid
   AND
   c.name LIKE '%-DNA')
Where s.name IN ('SA-62-Plate_1-E03')
```
