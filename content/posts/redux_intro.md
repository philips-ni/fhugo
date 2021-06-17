+++
title = "Redux intro"
author = ["Fei Ni"]
date = 2021-06-04T23:54:38-07:00
lastmod = 2021-06-04T23:54:38-07:00
tags = ["helix"]
categories = ["helix"]
draft = false
+++

## <span class="section-num">1</span> Vocabulary {#vocabulary}

-   Redux - a library that allows JavaScript apps to manage application state
-   action - an object containing a type and a payload, used to tell the reducer how to update the store
-   action creator - a function that takes in a payload and creates an action object
-   reducer - a function that takes in the initial state and an action, and which returns that specific part of the global store
-   combineReducers - a function from Redux that allows us to put together all our reducers into a single object (often called the rootReducer)
-   store/global state - an object; think of it as a mega state that is accessed and updated with its own functions (similar to how React state is updated with setState)
-   createStore - a function from Redux that uses the rootReducer to create the store
-   dispatch - a function from Redux that sends an action object to its reducer (which updates the store)
-   Provider - a component from react-redux that wraps our App component and allows each child component to be connected to the store
-   mapStateToProps - a function we create that takes in the global state object and returns an object to be added to a component as part of its props object; it allows the component to access the data in the store
-   mapDispatchToProps - a function we create that takes in dispatch and returns an object to be added to a component as part of its props object; it allows the component to update the data in the store
-   connect - a function from react-redux that allows us to connect a component to the store by adding items from the store to our component props, as well as adding dispatch to our component props
-   container - what we call a component that has been connected to the store


## <span class="section-num">2</span> Links {#links}

-   <https://github.com/rt2zz/redux-persist>
-   <http://www.ruanyifeng.com/blog/2016/09/redux%5Ftutorial%5Fpart%5Fone%5Fbasic%5Fusages.html>
-   <https://frontend.turing.edu/lessons/module-3/redux-i.html?ads%5Fcmpid=6451354298&ads%5Fadid=76255849919&ads%5Fmatchtype=b&ads%5Fnetwork=g&ads%5Fcreative=378056926252&utm%5Fterm=&ads%5Ftargetid=dsa-19959388920&utm%5Fcampaign=&utm%5Fsource=adwords&utm%5Fmedium=ppc&ttv=2&gclid=Cj0KCQjwnueFBhChARIsAPu3YkR-bktINtaEkXQdkdj8S4KaJZgO9ydPzDXS5fOeH0v0dpeha76K-h0aAvILEALw%5FwcB>
