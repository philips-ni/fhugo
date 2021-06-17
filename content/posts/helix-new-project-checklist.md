+++
title = "New Helix project checklist"
author = ["Fei Ni"]
date = 2021-04-26T10:38:25-07:00
lastmod = 2021-04-26T10:38:25-07:00
tags = ["helix"]
categories = ["helix"]
draft = false
+++

## <span class="section-num">1</span> Prerequisite {#prerequisite}

-   Design doc reviewed and approved(see [this](https://myhelix.atlassian.net/wiki/spaces/ENG/pages/50268351/Architecture%2BReview))
-   For web application, consider to create 2 git repo(`{app}`, backend repo and `{app}-ui` , frontend repo)
-   For the backend repo, we can consider to create from this template:
    -   <https://github.com/myhelix/template-serverless-golang>
-   For the frontend repo, we can refer to this:
    -   <https://github.com/myhelix/hippo-ui>


## <span class="section-num">2</span> Switch Repo Over to RSDLC {#switch-repo-over-to-rsdlc}

```bash
$ touch VERSION
$ touch CHANGELOG
$ gco -b develp
Switched to a new branch 'develp'
[fei.ni@fei-ni-C02D72XMMD6N-SM  stt (develp %)]$ gb
* develp
  main
[fei.ni@fei-ni-C02D72XMMD6N-SM  stt (develp %)]$ gco developee
error: pathspec 'develop' did not match any file(s) known to git
[fei.ni@fei-ni-C02D72XMMD6N-SM  stt (develp %)]$ gb -d develp
error: Cannot delete branch 'develp' checked out at '/Users/fei.ni/gowork/src/github.com/myhelix/stt'
[fei.ni@fei-ni-C02D72XMMD6N-SM  stt (develp %)]$ gco main
Switched to branch 'main'
Your branch is up to date with 'origin/main'.
$ gb -d develp
Deleted branch develp (was 29248a6).
$ gco -b develop
Switched to a new branch 'develop'
$ gco develop
Already on 'develop'
$ rsdlc

Initializing git-flow

Using default branch names.

Which branch should be used for bringing forth production releases?
   - develop
   - main
Branch name for production releases: [main]

Which branch should be used for integration of the "next release"?
   - develop
Branch name for "next release" development: [develop]

How to name your supporting branch prefixes?
Feature branches? [feature/]
Bugfix branches? [bugfix/]
Release branches? [release/]
Hotfix branches? [hotfix/]
Support branches? [support/]
Version tag prefix? []
Hooks and filters directory? [/Users/fei.ni/devtools/git/hooks]

Setting default git-flow flags in git config

Linking git-flow hooks

Setup complete

```

Refer

-   <https://myhelix.atlassian.net/wiki/spaces/ENG/pages/674660439/Regulated+SDLC+2.0+git-flow+Playbook+rsdlc#Switching-to-RSDLC>
-   <https://myhelix.atlassian.net/wiki/spaces/ENG/pages/2100625542/How+to+Switch+a+Repo+Over+to+RSDLC>


## <span class="section-num">3</span> Setup circleCI {#setup-circleci}

-   <https://myhelix.atlassian.net/wiki/spaces/ENG/pages/1089504388/CircleCI+Setup>


## <span class="section-num">4</span> Update CDK code from the existing code of template {#update-cdk-code-from-the-existing-code-of-template}
