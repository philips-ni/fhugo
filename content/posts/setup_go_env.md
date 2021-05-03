+++
title = "Setup Golang env in mac"
author = ["Fei Ni"]
date = 2021-01-08
draft = false
+++

## <span class="section-num">1</span> Install brew {#install-brew}

-   <https://brew.sh/>

<!--listend-->

```bash
/usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
```


## <span class="section-num">2</span> Install go {#install-go}

-   brew install go


## <span class="section-num">3</span> Install go related tools {#install-go-related-tools}

```bash
% go get -u golang.org/x/tools/cmd/goimports
% go get -u github.com/rogpeppe/godef
% go get -u github.com/nsf/gocode
% go get -u golang.org/x/tools/gopls@latest
```
