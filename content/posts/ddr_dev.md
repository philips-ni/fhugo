+++
title = "Setup DDR development enviroment"
author = ["Fei Ni"]
date = 2021-04-27T18:24:31-07:00
lastmod = 2021-04-27T18:24:31-07:00
tags = ["helix"]
draft = false
+++

## <span class="section-num">1</span> Background {#background}

DDR(Data Delivery Review) is a internal work-flow website which is used to review the analysis report from the Helix platform by Helix tech reviewer manually.


## <span class="section-num">2</span> Related repos {#related-repos}

-   <https://github.com/myhelix/ddrui/>
-   <https://github.com/myhelix/ddr>


## <span class="section-num">3</span> Setup the local development environment {#setup-the-local-development-environment}


### <span class="section-num">3.1</span> [General helix dev setup](https://myhelix.atlassian.net/wiki/spaces/ENG/pages/31129602/Dev+Computer+Setup) {#general-helix-dev-setup}


### <span class="section-num">3.2</span> Setup and start the  backend {#setup-and-start-the-backend}

-   checkout the code from <https://github.com/myhelix/ddr>
-   hcd ddr
-   glide install
-   go install
-   go run main.go


### <span class="section-num">3.3</span> Start DB {#start-db}

-   rundeps (start the local db service)


### <span class="section-num">3.4</span> Initialize DB {#initialize-db}

-   Setup local DB variable and run data migration

    ```bash
    export DB_USER=root
    export DB_PASS=
    export DB_HOST=127.0.0.1
    export DB_PORT=3181
    dbauth migration goose --env test up
    ```

-   Insert yourself into reviewerUsers table

<!--listend-->

```bash
#enter mysql console
docker exec -it docker_mysql-ddr_1 mysql ddr
# insert yourself into reviewUsers table, so that you can login in at the first place
mysql> insert into reviewUsers (userId, userRoles, isActive) values ('ross.blanchard@helix.com', 'CLS,LabDirector,Expert,Admin', true)
```


### <span class="section-num">3.5</span> Setup and start front-end {#setup-and-start-front-end}

-   Install required packages
    -   brew install node yarn flow
-   checkout the code from <https://github.com/myhelix/ddrui/>
-   hcd ddrui
-   yarn
-   yarn dev (It will open a browser and show the login page)


## <span class="section-num">4</span> client Ids {#client-ids}

| Env        | google\_client\_id                                                       |
|------------|--------------------------------------------------------------------------|
| staging    | 581178163594-2gdjneq9sbcc71gcuaesk4akgfd6d7qv.apps.googleusercontent.com |
| test       | 581178163594-6rgulcirk2grvv5bbl0t5j9sq2lsvif6.apps.googleusercontent.com |
| production | 581178163594-s1lsfae3r1uca003pq4egdoukr8v0ba6.apps.googleusercontent.com |
