+++
title = "Ascii graph creator"
author = ["Fei Ni"]
date = 2019-11-30
draft = false
+++

## <span class="section-num">1</span> GraphViz {#graphviz}

-   <https://renenyffenegger.ch/notes/tools/Graphviz/examples/index>


## <span class="section-num">2</span> Online service {#online-service}

-   <https://dot-to-ascii.ggerganov.com/>


## <span class="section-num">3</span> Examples {#examples}


### <span class="section-num">3.1</span> dots content {#dots-content}

```bash
graph{
        rankdir = LR;
        a -- b;
        b -- c;
        a -- c;
        d -- c;
        e -- c;
        e -- a;
}
```


### <span class="section-num">3.2</span> Ascii output {#ascii-output}

```bash
            +-------------------+
            |                   |
+---+     +---+     +---+     +---+     +---+
| d | --- |   | --- | e | --- | a | --- | b |
+---+     | c |     +---+     +---+     +---+
          |   |                           |
          |   | --------------------------+
          +---+

```
