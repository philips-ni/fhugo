+++
title = "Docker tips"
author = ["Fei Ni"]
date = 2019-10-22
tags = ["docker"]
categories = ["docker"]
draft = false
+++

## <span class="section-num">1</span> mount nfs share from a docker container {#mount-nfs-share-from-a-docker-container}

```bash
nsenter --mount=/proc/9218/ns/mnt mount -t nfs 10.84.179.253:/nbuappliance/tools /mnt
```

**9218** is comming from:

```bash
[root@davidcl02vm110 ~]#  docker inspect --format {{.State.Pid}} 7e50517a93d1
9218
```

**7e50517a93d1** is coming from :

```nil
[root@davidcl02vm110 ~]#  docker ps -a
CONTAINER ID        IMAGE                                  COMMAND                  CREATED             STATUS                PORTS                                                            NAMES
7e50517a93d1        netbackup/main:8.1.2                   "/usr/sbin/init"         3 days ago          Up 3 days (healthy)                                                                    davidcl02vm110app1
748be5f56860        netbackup/tool:8.1.2                   "bash"                   3 days ago          Created                                                                                HDUg_tool
f3f72ae7964f        veritas/flex/webui:latest              "/usr/sbin/nginx -..."   3 days ago          Up 3 days (healthy)   10.85.16.188:443->443/tcp, 80/tcp, 10.85.16.188:8443->8443/tcp   webui
ecde07d8bf73        veritas/flex/mgmtserver:latest         "/bin/sh -c /VRTSa..."   3 days ago          Up 3 days (healthy)   8080/tcp                                                         mgmtserver
dce6515223e8        veritas/appliance/authservice:latest   "/opt/veritas/appl..."   3 days ago          Up 3 days (healthy)   8081/tcp                                                         authservice
e509b4d5f71d        veritas/appliance/autosupport:latest   "/usr/sbin/init"         3 days ago          Up 3 days (healthy)
```
