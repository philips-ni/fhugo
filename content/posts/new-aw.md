+++
title = "Analysis workflow V2"
author = ["Fei Ni"]
date = 2022-04-01
lastmod = 2022-04-01T11:55:18-07:00
tags = ["helix"]
draft = false
+++

## <span class="section-num">1</span> Facts {#facts}

-   R2V is common, and should be done before for other analysises.
-   Some analysises may depend on all output data of R2V job (per batch/pool
-   Some analysises may only depend on the particular sample's r2v output (per sample)
-   Some analysises are required to be reviwed by person ( need be placed before pushing to R2V)
-   Some analysises are not required to be reviewed by person (need be placed after pushing to R2V)
-   Each analysis may generate metrics(tied with analysisID) for their own with their own logic (current we put such logic into lab library, which may not goot for **plug and play** model)
-   the metadataJson from R2V job is the input for other analysises which are required review


## <span class="section-num">2</span> Questions: {#questions}

-   for each analysises type, will they only depend on R2V? is it possible some analysis type may depend on antoher analysis type?
