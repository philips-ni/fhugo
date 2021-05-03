+++
title = "Setup my Emacs env"
author = ["Fei Ni"]
date = 2019-01-16
categories = ["emacs"]
draft = false
+++

## <span class="section-num">1</span> Download Emacs 26.1 {#download-emacs-26-dot-1}

```nil
wget https://ftp.gnu.org/pub/gnu/emacs/emacs-26.1.tar.gz
```


## <span class="section-num">2</span> Untar it {#untar-it}

```nil
tar -zxvf emacs-26.1.tar.gz
```


## <span class="section-num">3</span> Compile and install it {#compile-and-install-it}

```nil
./configure --with-x-toolkit=no  --with-xpm=no --with-gif=no --with-gnutls=no
make
make install
```


## <span class="section-num">4</span> Checkout .emacs.d {#checkout-dot-emacs-dot-d}

```nil
git clone https://FeiPhilips.Ni@stash.veritas.com/scm/\~feiphilips.ni/emacs.d.git ~/.emacs.d
```


## <span class="section-num">5</span> Setup my emacs configuration {#setup-my-emacs-configuration}

```nil
# just start emacs, it will automatically download required packages and complete the configuration
emacs
```


## <span class="section-num">6</span> Setup lsp (Language Server Protocol) {#setup-lsp--language-server-protocol}

-   <https://www.mortens.dev/blog/emacs-and-the-language-server-protocol/>
