+++
title = "Add uses into accessioning UI"
author = ["Fei Ni"]
date = 2021-05-18T12:52:45-07:00
lastmod = 2021-05-18T12:52:45-07:00
tags = ["helix"]
categories = ["helix"]
draft = false
+++

## <span class="section-num">1</span> Env setup {#env-setup}

-   in aws\_profile Master-oncall
-   using aws production VPN


## <span class="section-num">2</span> Accessing DB {#accessing-db}

```bash
$ PGPASSWORD='W*2AAnQdWWWHw8OowmGs' psql accessioning  --host=accessioning-aurora-hipaa.cluster-ctc4k8bzul0z.us-east-1.rds.amazonaws.com --port=5432 --user='accessioning-service'
```


## <span class="section-num">3</span> SQL {#sql}

```bash
BEGIN;
INSERT INTO users (user_email, role) VALUES
('jennifer.corona@helix.com','STAFF'),
('maryam.kako@helix.com', 'STAFF'),
('reanna.hutalla@helix.com', 'STAFF'),
('mimi.luong@helix.com', 'STAFF'),
('tatyana.lemus@helix.com', 'STAFF'),
('trang.vu@helix.com', 'STAFF'),
('sonia.bouathong@helix.com', 'STAFF'),
('marco.villascueza@helix.com', 'STAFF'),
;
COMMIT;
```


## <span class="section-num">4</span> Links {#links}

-   <https://myhelix.atlassian.net/wiki/spaces/PS/pages/1947828747/How+to+add+Users+to+Accessioning+HAMUI>
