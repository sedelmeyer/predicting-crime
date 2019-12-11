---
title: "Results"
---

## Literature Review/Related Work

This project relied heavily on public datasets made available by the City of Boston [https://data.boston.gov/dataset](https://data.boston.gov/dataset) and [https://data.boston.gov/dataset](http://bostonopendata-boston.opendata.arcgis.com/datasets/).  

Our approach was not influenced by any other projects that have looked at this problem in the past.  We wanted to tackle this issue with a fresh set of eyes.  We performed extensive EDA on datasets that we believed would have an impact on crime type.  A large portion of this project was focused on determining the appropriate predictors and feature generation.  

We relied heavily on course materials from [Harvard University’s CS 109a](https://github.com/Harvard-IACS/2019-CS109A) and online resources to help guide us as we coded this project.  Some of the websites we used are listed below:

-	[https://www.stackoverflow.com/](https://www.stackoverflow.com/)
-	[https://stats.stackexchange.com/](https://stats.stackexchange.com/)
-	[https://medium.com/](https://medium.com/)

## Modeling Approach

Please refer to our [**Models**](models.md) page for a deeper dive into our approach. 

We first ran a [Baseline Logistic Classifier](model-baseline.md) with just the ``lat`` and ``lon`` as predictors to determine how exclusively important these spatial variables were.  This resulted in a test data accuracy of **0.273** without balancing and **0.133** with balancing.  

> The unbalanced model simply predicted every crime as either classes 4 (harassment-disturbance) and 6 (theft).

## Project Trajectory, Results, and Interpretation

Briefly summarize any changes in your project goals or implementation plans you have made along the way. These changes are a natural part of any project, even those that seem the most straightforward at the beginning. The story you tell about how you arrived at your results can powerfully illustrate your process. Next, show your results. How well does your model and/or implementation perform? Did you meet your goals? Finally, give some interpretation. What do your results mean? What impact will your work have?

## Conclusions and Future Work 

Summarize your results, the strengths and short-comings of your results, and speculate on how you might address these short-comings if given more time.
