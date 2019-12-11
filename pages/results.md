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

#### Please refer to our [**Models**](models.md) page for a deeper dive into our approach.

&nbsp;

We first ran a [**Baseline Logistic Classifier**](model-baseline.md) with just the ``lat`` and ``lon`` as predictors to determine how exclusively important these spatial variables were.  This resulted in a test data ``accuracy score`` of **0.273** without balancing and **0.133** with balancing.  

*The unbalanced model simply predicted every crime as either class 4 (harassment-disturbance) and class 6 (theft).*

&nbsp;

Next we ran the [**Logistic Classifier**](model-logistic.md) on our full-set of predictors with and without regularization.  This model provides the benefit of interpretable results, from which we can begin to develop a better understanding of the relationships between specific predictors and response classes.

*Given the geographical inter-mixing of our response classes and the high bias of these results, we suspect that the linear decision boundaries of a logistic function are not expressive enough for accurately defining our feature space and predicting results.*

&nbsp;

Our [**KNN Classifier**](model-knn.md) after tuning resulted in a test data ``accuracy score`` of **0.346** and a ``weighted AUC`` of **0.661**.  This model was especially good at predicting class 2 (drug_substances) with a ``True Positive Rate (TPR)`` of **0.499**.  *Please refer to the KNN model page for the full confusion matrix*.

We also ran our KNN model on a subset of the data with three crime classes.  On this subset of data the model achieved an ``accuracy score`` of **0.603** and ``weighted AUC`` of **0.741**.  

> How the data is subset and how the categories are chosen can greatly impact the accuracy our models achieve. Our framework is extensible enough to accommodate for different subsets and categories based on requirements.

&nbsp;

Our [**Decision Trees**](model-trees.md) models included a single decision tree, bagging an overfit tree, boosting an underfit tree and random forest.  Random forest gave us the best scores on the test data with an ``accuracy score`` of **0.350** and ``weighted AUC`` of **0.561**.

The single decision tree provided allowed us to determine feature importances of our predictors which were extremely insightful.  The most important features in order of importance were: ``lon``, ``lat``, ``bachelor-degree-or-more-perc``, ``commercial-mix-ratio``, ``industrial-mix-ratio``, ``tempavg``, ... 

&nbsp;

[**Feed Forward Artificial Neural Network**](model-ann.md)

&nbsp;

## Project Trajectory, Results, and Interpretation

During the course of this project we had to shift our implementation multiple times given our EDA of the datasets.  Some datasets ended up being abandoned because they either had missing data or not enough data for our analysis *(for example liquor license data)*.  We also decided that ``lat`` and ``lon`` be part of any data we used to associate it with the ``lat`` and ``lon`` in the crime dataset.

We also shifted what our output of this project would be given time constraints.  We initially planned on having the user input a ``lat``, ``lon`` and other predictors into the model to calculate probabilities of each type of crime.  For this iteration our model spilts the crime dataset into train and test data and then predicts the type of crime in the test data. 

&nbsp;

## Conclusions and Future Work 

Summarize your results, the strengths and short-comings of your results, and speculate on how you might address these short-comings if given more time.
