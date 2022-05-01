+++
title = "My toolchain for development"
author = ["Fei Ni"]
date = 2022-04-09
lastmod = 2022-04-13T12:58:45-07:00
tags = ["tools"]
categories = ["tools"]
draft = false
+++

## <span class="section-num">1</span> My toolchain for development {#my-toolchain-for-development}


### <span class="section-num">1.1</span> My daily work {#my-daily-work}

As a software engineer, my daily work includes:

-   Coding
-   Writting Docs/Notes
-   Build and test (Build enviroment setup)
-   Communication (Slack/Teams/Zoom + Chrome/Gmail/Jira)


### <span class="section-num">1.2</span> tools {#tools}

{{< figure src="../../images/tools.png" >}}


## <span class="section-num">2</span> Iterm2 + Tmux + HomeBrew for terminal work {#iterm2-plus-tmux-plus-homebrew-for-terminal-work}


### <span class="section-num">2.1</span> Iterm2 {#iterm2}

-   nice default profile with awesome color/fonts
-   copy on select
-   split windows horizontally or vertically with shortcut keys
-   [Iterm2 tips and tricks](https://gist.github.com/tanyuan/a1a3c00b9c231c32c3613d4bbefa6652)
-   [5-useful-iterm2-features-for-developers](https://betterprogramming.pub/5-useful-iterm2-features-for-developers-bc211d697817)


### <span class="section-num">2.2</span> Homebrew {#homebrew}

Homebrew is a `package manager` for the mac OS to search,
install and configure software packages and libraries through the command line.
It simplifies the package installation by automatically finding and installing the
dependencies when you are installing a package.

```bash

brew install tmux
brew install emacs
```

-   <https://brew.sh/>


### <span class="section-num">2.3</span> Tmux {#tmux}

-   Session handling: detaching from and attaching to sessions helps me with
    context switching and remote working
-   multiple windows support
-   It's very useful while working with remote server, so that you can keep your
    workspace all the time, and don't need worry about your ssh session diconnected


## <span class="section-num">3</span> Emacs for all kinds of development work {#emacs-for-all-kinds-of-development-work}

Emacs works great in both terminal


### <span class="section-num">3.1</span> Git plugin (magit) {#git-plugin--magit}

-   Best Git client I have used
-   C-x g to pop it up
-   [magit reference](https://www.masteringemacs.org/article/introduction-magit-emacs-mode-git)


### <span class="section-num">3.2</span> Coding {#coding}

-   LSP (language server protocol)
    -   auto completion
    -   jump to definition and jump back
        -   C-. and C-,
    -   flycheck
-   Search keyword and jump to there
-   bookmark for those hotspots


### <span class="section-num">3.3</span> Document/Notes writing with org mode {#document-notes-writing-with-org-mode}


#### <span class="section-num">3.3.1</span> Notes manager {#notes-manager}

-   C-c c, take/capture notes at any time
-   [how to take smart notes](https://blog.jethro.dev/posts/how%5Fto%5Ftake%5Fsmart%5Fnotes%5Forg/)


#### <span class="section-num">3.3.2</span> outline view/switching {#outline-view-switching}


#### <span class="section-num">3.3.3</span> Table {#table}

-   Easy to create table
-   Easy to swap columns and rows
    -   M-LEFT, M-RIGHT (for columns)
    -   M-UP, M-DOWN (for rows)
-   Easy to insert new column or delete current column
    -   M-S-LEFT(delete current column)
    -   M-S-RIGHT(insert a new column)

| Student  | Maths | Physics | Mean | Sum |
|----------|-------|---------|------|-----|
| Bertrand | 13    | 09      |      |     |
| Henri    | 15    | 14      |      |     |
| Arnold   | 17    | 13      |      |     |

-   move to TBLFM line, press C-c C-C, it will trigger the calculation


#### <span class="section-num">3.3.4</span> FlowChart {#flowchart}

```text
digraph D {
{rank=same A, E}
A -> B [stylde=dashed, color=grey]
A -> C [color="black:invis:black"]
A -> D [penwidth=5, arrowhead=none]
D -> E
E -> F
}

```

{{< figure src="../../images/test1.png" >}}


#### <span class="section-num">3.3.5</span> export to markdown/html/pdf {#export-to-markdown-html-pdf}
