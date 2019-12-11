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

&nbsp;

## Modeling Approach

*Please refer to our [**Models**](models.md) page for a deeper dive into our approach.*

[**Baseline Logistic Classifier**](model-baseline.md)

We first ran a the logistic classifier with just the ``lat`` and ``lon`` as predictors to determine how exclusively important these spatial variables were.  This resulted in a test data ``accuracy score`` of **0.273** without balancing and **0.133** with balancing.  

*The unbalanced model simply predicted every crime as either class 4 (harassment-disturbance) and class 6 (theft).*

[**Logistic Classifier**](model-logistic.md)

Next we ran the logistic classifier on our full-set of predictors with and without regularization.  This model provides the benefit of interpretable results, from which we can begin to develop a better understanding of the relationships between specific predictors and response classes.

*Given the geographical inter-mixing of our response classes and the high bias of these results, we suspect that the linear decision boundaries of a logistic function are not expressive enough for accurately defining our feature space and predicting results.*

[**KNN Classifier**](model-knn.md) 

Our after tuning KNN classifier resulted in a test data ``accuracy score`` of **0.346** and a ``weighted AUC`` of **0.661**.  This model was especially good at predicting class 2 (drug_substances) with a ``True Positive Rate (TPR)`` of **0.499**.  *Please refer to the KNN model page for the full confusion matrix*.

We also ran our KNN model on a subset of the data with three crime classes.  On this subset of data the model achieved an ``accuracy score`` of **0.603** and ``weighted AUC`` of **0.741**.  

> How the data is subset and how the categories are chosen can greatly impact the accuracy our models achieve. Our framework is extensible enough to accommodate for different subsets and categories based on requirements.

[**Decision Trees**](model-trees.md)

Our tree models included a single decision tree, bagging an overfit tree, boosting an underfit tree and random forest.  Random forest gave us the best scores on the test data with an ``accuracy score`` of **0.350** and ``weighted AUC`` of **0.561**.

The single decision tree provided allowed us to determine feature importances of our predictors which were extremely insightful.  The most important features in order of importance were: ``lon``, ``lat``, ``bachelor-degree-or-more-perc``, ``commercial-mix-ratio``, ``industrial-mix-ratio``, ``tempavg``, ... 

[**Feed Forward Artificial Neural Network**](model-nn.md)

Fabio's findings

&nbsp;

## Project Trajectory, Results, and Interpretation

During the course of this project we had to shift our implementation multiple times given our EDA of the datasets.  Some datasets ended up being abandoned because they either had missing data or not enough data for our analysis *(for example liquor license data)*.  We also decided that ``lat`` and ``lon`` be part of any data we used to associate it with the ``lat`` and ``lon`` in the crime dataset.

We also shifted what our output of this project would be given time constraints.  We initially planned on having the user input a ``lat``, ``lon`` and other predictors into the model to calculate probabilities of each type of crime.  For this iteration our model spilts the crime dataset into train and test data and then predicts the type of crime in the test data. 

The full analysis of each models output is discussed in detail in each individual model page.  Our best models have an ``accuracy score`` of around **0.35** on a multi-class categorization problem with nine different crime types.  This is much better than chance so our predictor do have predictive power but not as high as our goals.  We believe that the way the crimes are categorized and subset has a huge impact on accuracy.  On subsets of our data with the categories defined differently, we can achieve much higher accuracy scores.  Therefore, our models will perform much more in line with our goals on specific tasks.  The task of predicting all crime types across all of Boston for the last few years is too broad to get high accuracies *(in a small city like Boston a large number of crimes results in a spatial distribution that is spread across the city)*.

Especially interesting are the relationships of crime type to ``bachelor-degree-or-more-perc``, ``commercial-mix-ratio``, ``industrial-mix-ratio`` and ``tempavg``.  We did not predict that bachelor degree percentage would have such a high importance.  The interpretability graphs at the end of the [Neural Network](model-nn.md) page also show very interesting relationships between our predictors and different crime types.

Our models show that it is possible to predict the probability of different crime types.  The accuracy is currently not as high as we desire but by adding additional features and making the problem more specific we believe sufficient accuracies can be achieved for the model to be useful.  Police departments and other city departments can use the model to appropriately distribute staff across Boston.  

&nbsp;

## Conclusions and Future Work 

Our results show a lot of promise and a subset of our predictors are significant for predicting the type of crime.  In the future, we will explore further datasets and generate more features using the existing data to further explore the type of predictors that are significant for predicting crime.  We also still have some issues with missingness and collinearity in several of our features (collinearity information is included in Appendix 2) which we will resolve in future iterations.

We plan on further exploring each of the raw ``OFFENSE_CODE_GROUP`` values and how they are distributed across each of our predictors.  This will help us understand which ``OFFENSE_CODE_GROUP`` values can be differentiated by out predictors.  The present grouping of these code groups into crime categories might be masking the influence of the individual crime codes.  Our subset data was the beginning of our exploration of how the crime categories affect our models.

Finally, we will be adding a function to this project that when input ``lat``, ``lon``, ``night``, ``temp``, ect can predict the probability of each crime type.  

