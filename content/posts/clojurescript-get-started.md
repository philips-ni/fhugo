+++
title = "Clojurescript get started"
author = ["Fei Ni"]
date = 2019-06-15
tags = ["clojure"]
draft = false
+++

## <span class="section-num">1</span> Env {#env}

-   RHEL 7.6


## <span class="section-num">2</span> Install Leiningen {#install-leiningen}

-   curl -O /usr/bin/lein  <https://raw.githubusercontent.com/technomancy/leiningen/stable/bin/lein>


## <span class="section-num">3</span> Create project with figwheel template {#create-project-with-figwheel-template}

-   lein new figwheel it-works


## <span class="section-num">4</span> Start figwheel repl {#start-figwheel-repl}

-   cd it-works
-   lein figwheel

Notice: only if you access <http://0.0.0.0:3449> from the server, the repl console will be appear

```nil
➜  it-works lein figwheel
Figwheel: Cutting some fruit, just a sec ...
Figwheel: Validating the configuration found in project.clj
Figwheel: Configuration Valid ;)
Figwheel: Starting server at http://0.0.0.0:3449
Figwheel: Watching build - dev
Compiling build :dev to "resources/public/js/compiled/it_works.js" from ["src"]...
Successfully compiled build :dev to "resources/public/js/compiled/it_works.js" in 1.11 seconds.
Figwheel: Starting CSS Watcher for paths  ["resources/public/css"]
Launching ClojureScript REPL for build: dev
Figwheel Controls:
          (stop-autobuild)                ;; stops Figwheel autobuilder
          (start-autobuild id ...)        ;; starts autobuilder focused on optional ids
          (switch-to-build id ...)        ;; switches autobuilder to different build
          (reset-autobuild)               ;; stops, cleans, and starts autobuilder
          (reload-config)                 ;; reloads build config and resets autobuild
          (build-once id ...)             ;; builds source one time
          (clean-builds id ..)            ;; deletes compiled cljs target files
          (print-config id ...)           ;; prints out build configurations
          (fig-status)                    ;; displays current state of system
          (figwheel.client/set-autoload false)    ;; will turn autoloading off
          (figwheel.client/set-repl-pprint false) ;; will turn pretty printing off
  Switch REPL build focus:
          :cljs/quit                      ;; allows you to switch REPL to another build
    Docs: (doc function-name-here)
    Exit: :cljs/quit
 Results: Stored in vars *1, *2, *3, *e holds last exception object
Prompt will show when Figwheel connects to your application
[Rebel readline] Type :repl/help for online help info
ClojureScript 1.10.238
dev:cljs.user=>

```


## <span class="section-num">5</span> Test the Repl {#test-the-repl}

```nil
dev:cljs.user=> (js/alert "Hi from Figwheel Again!")
```

It will pop a windows in your browser window


## <span class="section-num">6</span> Emacs configuration {#emacs-configuration}


### <span class="section-num">6.1</span> Install cider {#install-cider}


### <span class="section-num">6.2</span> create ~/.lein/project.clj {#create-dot-lein-project-dot-clj}

```nil
{:user {:plugins [[cider/cider-nrepl "0.21.1"]]}}
```


## <span class="section-num">7</span> Reference {#reference}

-   <https://www.braveclojure.com/getting-started/>
-   <https://lionfacelemonface.wordpress.com/2015/01/17/boot-getting-started-with-clojure-in-10-minutes/>
-   <https://www.braveclojure.com/getting-started/>
