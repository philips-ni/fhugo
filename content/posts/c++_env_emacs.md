+++
title = "Setup C++ Dev environment in Emacs"
author = ["Fei Ni"]
date = 2019-11-03
draft = false
+++

## <span class="section-num">1</span> Intro {#intro}

This doc is based Ubuntu 19

Refer to <https://www.sandeepnambiar.com/setting-up-emacs-for-c++/>


## <span class="section-num">2</span> Install cmake {#install-cmake}

-   sudo apt-get install cmake


## <span class="section-num">3</span> build and install ccls {#build-and-install-ccls}

```nil
sudo apt install zlib1g-dev libncurses-dev clang
git clone --depth=1 --recursive https://github.com/MaskRay/ccls
cmake -H. -BRelease -DCMAKE_BUILD_TYPE=Release \
    -DCMAKE_PREFIX_PATH=/usr/lib/llvm-7 \
    -DLLVM_INCLUDE_DIR=/usr/lib/llvm-7/include \
    -DLLVM_BUILD_INCLUDE_DIR=/usr/include/llvm-7/
cmake --build Release --target install
```


## <span class="section-num">4</span> install ctags and ggtags {#install-ctags-and-ggtags}

-   sudo apt-get isntall ctags global
-   install ggtags in emacs


## <span class="section-num">5</span> install lsp for c++ {#install-lsp-for-c}

-   lsp-mode
-   lsp-ui


## <span class="section-num">6</span> Reference {#reference}

-   <https://www.sandeepnambiar.com/setting-up-emacs-for-c++/>
