---
title: "CST User Workflow"
date: 2021-04-21T09:20:40-07:00
draft: false
tags:
  - helix
---


John is a lab member, firstly he login in  CST website with DUO authentication, he saw a list of samples which are pending for `confirmatory testing`, in this list it's showing:
  * sampleID
  * sample plate location info
  * sufficient DNA?
  * importedAt


From this list, he just filters out with `"sufficient DNA?" ==  "pending"`, and sorted by `importedAt`, he gets a new list and record this list in a paper (maybe we can support export and print in the future), then he comes to lab to find out the plates for those samples to check and record "Sufficient DNNA?" information.
After John completes his work in the lab, he comes back to his desktop, input those "Sufficient DNA" into CST website. And he just selects all `"sufficent DNA?" == "no"` samples and click `return to PHP` button to return them back.
In the meantime, he notices only 2 samples are identified to be ready to send out for "confirmatory testing", so he does not create the order.


In the afternoon, John logins CST website again, he noticed there are more pending samples showing in the list, so he repeats morning's work, now it turns our there are 10 samples which are ready to be sent for "confirmatory testing", so he selects all of them and click "place order" button. after that he just sees a order confirmation page, from this page, he can see the manifest of this order, and he can input `tracking number` there, then he click "ok" button, those samples are sent for "confirmatory testing" and John see a order detail page, from this page he is able to print the order manifest for his shipment.

