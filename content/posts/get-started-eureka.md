---
title: "Eureka Get Started"
date: 2021-04-20T08:51:33-07:00
draft: false
tags:
  - hugo
---
### Prepare Hugo env
  * [Install Hugo](https://gohugo.io/getting-started/installing/)
### Prepare Eureka
  * [Setup Eureka](https://www.wangchucheng.com/en/docs/hugo-eureka/getting-started)

### Update configuration
  * Update `title` in config/config.yaml
  * Update `baseURL` in config/config.yaml
  * Update `paginate` in config/config.yaml
  * Update `copyrigt` in config/config.yaml

### Start service

```
 hugo server -p 8080 --bind 192.168.1.112 -b http://192.168.1.112:8080
```

### Common operations
  * Create a post
```
  hugo new posts/get-started-eureka.md
```
