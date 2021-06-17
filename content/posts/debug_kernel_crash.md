+++
title = "Debug Kernel crash"
author = ["Fei Ni"]
date = 2019-01-10
categories = ["kernel"]
draft = false
+++

## <span class="section-num">1</span> Setup the yum repo {#setup-the-yum-repo}

-   Create a file /etc/yum.repos.d/vxos-rhel-7-server-debug-rpms.repo

```nil
#cat /etc/yum.repos.d/vxos-rhel-7-server-debug-rpms.repo
[vxos-rhel-7-server-debug-rpms]
name=vxos-rhel-7-server-debug-rpms
baseurl=http://artifactory-appliance.engba.veritas.com/artifactory/vxos-rhel7-debug-cache
enable=1
gpgcheck=0
[Artifactory]
name=Artifactory
baseurl=http://artifactory-appliance.engba.veritas.com/artifactory/yum-build-tools/rhel7/
enabled=1
gpgcheck=0
[vxos-rhel7-server]
name=vxos-rhel7-server
baseurl=http://artifactory-appliance.engba.veritas.com/artifactory/vxos-rhel7-server
gpgcheck=no
enabled=1

[vxos-rhel7-server-extras]
name=vxos-rhel7-server-extras
baseurl=http://artifactory-appliance.engba.veritas.com/artifactory/vxos-rhel7-server-extras
gpgcheck=no
enabled=1

[vxos-7-epel]
name=vxos-epel7
baseurl=http://artifactory-appliance.engba.veritas.com/artifactory/vxos-epel7/


[vxos-rhel-7-server-optional-rpms]
name=vxos-rhel-7-server-optional-rpms
baseurl=http://rsvlmvc01vm385.rmnus.sen.symantec.com/vxos-rhel-7-server-optional-rpms/
enable=1
gpgcheck=0
```


## <span class="section-num">2</span> Install required rpms {#install-required-rpms}

```nil
debuginfo-install kernel
yum install crash
```


## <span class="section-num">3</span> Run Crash to analysis {#run-crash-to-analysis}

```nil
crash /usr/lib/debug/lib/modules/<kernel_ver>/vmlinux <path/to/dump>
```
