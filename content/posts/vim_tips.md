+++
title = "VIM tips"
author = ["Fei Ni"]
date = 2019-01-06
categories = ["vim"]
draft = false
+++

## <span class="section-num">1</span> Append '#' at the beginning of each lines {#append-at-the-beginning-of-each-lines}

```nil
:%normal I#
```


## <span class="section-num">2</span> Append ';' at the end of  each lines {#append-at-the-end-of-each-lines}

```nil
:%normal A;
```


## <span class="section-num">3</span> Search text in a directory {#search-text-in-a-directory}

```nil
:vimgrep def **/*.py
```


## <span class="section-num">4</span> Multiple windows {#multiple-windows}

```nil
:e filename      - edit another file
:split filename  - split window and load another file
ctrl-w up arrow  - move cursor up a window
ctrl-w down arrow  - move cursor down a window
ctrl-w left arrow  - move cursor to left window
ctrl-w right arrow  - move cursor to right window
ctrl-w ctrl-w    - move cursor to another window (cycle)
ctrl-w_          - maximize current window
ctrl-w=          - make all equal size
10 ctrl-w+       - increase window size by 10 lines
ctrl-w s         - split
ctrl-w v         - vertical split
:vsplit file     - vertical split
:sview file      - same as split, but readonly
:hide            - close current window
:only            - keep only this window open
:ls              - show current buffers
:b 2             - open buffer #2 in this window
```


## <span class="section-num">5</span> Sort specified line inline {#sort-specified-line-inline}

```nil
:2,$!sort -k2r
```


## <span class="section-num">6</span> Auto completion {#auto-completion}

```nil
Typing is a pain! In insert mode, try:

ctrl-n, ctrl-p    - next/previous word completion
                    (similar word in current file)

ctrl-x ctrl-l (ctrl-n/p)    - line completion

:set dictionary=/usr/share/dict/words
ctrl-x ctrl-k     - dictionary completion
also

ctrl-w      - erases word (insert mode...
ctrl-u      - erases line  ...or on command line)
```


## <span class="section-num">7</span> Multiple windows {#multiple-windows}

```nil
:e filename      - edit another file
:split filename  - split window and load another file
ctrl-w up arrow  - move cursor up a window
ctrl-w ctrl-w    - move cursor to another window (cycle)
ctrl-w_          - maximize current window
ctrl-w=          - make all equal size
10 ctrl-w+       - increase window size by 10 lines
:vsplit file     - vertical split
:sview file      - same as split, but readonly
:hide            - close current window
:only            - keep only this window open
:ls              - show current buffers
:b 2             - open buffer #2 in this window
```


## <span class="section-num">8</span> Cursor movement {#cursor-movement}

```nil
h - move left
j - move down
k - move up
l - move right
w - jump by start of words (punctuation considered words)
W - jump by words (spaces separate words)
e - jump to end of words (punctuation considered words)
E - jump to end of words (no punctuation)
b - jump backward by words (punctuation considered words)
B - jump backward by words (no punctuation)
0 - (zero) start of line
^ - first non-blank character of line
$ - end of line
G - Go To command (prefix with number - 5G goes to line 5)

CTRL-u page up
CTRL-d page down
```


## <span class="section-num">9</span> Reference {#reference}

-   <https://www.cs.oberlin.edu/~kuperman/help/vim>
-   <https://vim.rtorr.com/>
-   <https://www.thegeekstuff.com/2009/03/8-essential-vim-editor-navigation-fundamentals/>
