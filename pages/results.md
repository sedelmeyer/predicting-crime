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

We first ran a logistic classifier with just the ``lat`` and ``lon`` as predictors to determine how exclusively important these spatial variables were.  This resulted in a test data ``accuracy score`` of just **0.273** without class weightings and **0.133** with "balanced" class weightings.

Something notable is that, due to the heavy imbalances in `crime-type` response classes, our model simply predicted every crime as either class 4 (harassment-disturbance) and class 6 (theft). And while, by balancing weights, our model provided predictions for all classes, our overall accuracy began to suffer. [A more nuanced breakdown of this relationship between predictions and weighting can be viewed here](model-baseline.md#confmat).

[**Logistic Classifier**](model-logistic.md)

Next we ran the logistic classifier on [our full-set of predictors](models.md#predictors) with and without cross-validated lasso regularization.  This model provides the benefit of interpretable results, from which we can begin to develop a better understanding of the relationships between specific predictors and response classes, [as can be seen on the logistic model results page here](model-logistic.md#coef). With these models we achieved small improvements in our `accuracy score` which was **0.2977** for our best model without class weight balancing and **21.33** with balancing. What is notable is the increase we achieved in ``weighted AUC`` in both instances, the best of which was **0.624** (up from **0.556** in our baseline). This increase in ``AUC`` provided far more favorable results, particularly noticable when [viewing our resulting ROC curves in these sets of models](model-logistic.md#roc1), versus [our original baseline](model-baseline.md#roc).

At this point, as a point of comparison, we also ran our logistic regression classifiers on observations for [a smaller subset of `crime-type` classes](models.md#response-comp) to better understand the effect of having fewer response classes, as well as a means to partially address the imbalances different `crime-types`. In these subset class models, we achieved a test ``accuracy score`` of 0.478 with a less than favorable `weighted AUC` of **0.577** [when using just `lat` and `lon` as our predictors](model-logistic.md#model3). Then, [with our entire predictor set, balanced class weights, and cross-validated lasso regularization](model-logistic.md#model4), our ``accuracy score`` was **0.451** and our ``weighted AUC`` was **0.644** with far more favorable ROC curves. 

However, it is important to caveat these logistic regression classifier results by stating that we still have [some outstanding issues of multi-collinearity in several of our underlying predictors](data.md#correlation), which is something we will need to address more fully in future iterations of this model.

[**KNN Classifier**](model-knn.md) 

Our after tuning KNN classifier resulted in a test data ``accuracy score`` of **0.346** and a ``weighted AUC`` of **0.661**.  This model was especially good at predicting class 2 (drug_substances) with a ``True Positive Rate (TPR)`` of **0.499**.  *Please refer to the KNN model page for the full confusion matrix*.

We also ran our KNN model on a subset of the data with three crime classes.  On this subset of data the model achieved an ``accuracy score`` of **0.603** and ``weighted AUC`` of **0.741**.  

> How the data is subset and how the categories are chosen can greatly impact the accuracy our models achieve. Our framework is extensible enough to accommodate for different subsets and categories based on requirements.

[**Decision Trees**](model-trees.md)

Our tree models included a single decision tree, bagging an over-fit tree, boosting an underfit tree and random forest.  Random forest gave us the best scores on the test data with an ``accuracy score`` of **0.350** and ``weighted AUC`` of **0.561**.

The single decision tree allowed us to determine feature importance of our predictors which were extremely insightful.  The most important features in order of importance were: ``lon``, ``lat``, ``bachelor-degree-or-more-perc``, ``commercial-mix-ratio``, ``industrial-mix-ratio``, and ``tempavg``. In addition, our random forest model illustrated similar top predictors especially with our location and education predictors .

We also ran our random forest on a subset of the data with three crime classes. On this subset of data the model achieved an ``accuracy score`` of **0.586** and ``weighted AUC`` of **0.738**

[**Feed Forward Artificial Neural Network**](model-nn.md)

For Neural Networks we started with a simple fast-training 3-layer fully connected network with 64 nodes which provided a ``weighted AUC`` of **0.498**.  Given that our simple model was overfitting we added dropout layers to our next model.  This model had similar performance in train and test and had an ``accuracy score`` of **0.307** and ``weighted AUC`` of **0.638** on test data.  We also ran a complex overnight model but the accuracy did not improve.

To derive insights into how each of the crime types are affected by the predictors we changed one predictor at a time while holding all the other predictors constant.  The output graphs in the Neural Network notebook provide an excellent visual tool to interpret how a predictor affects the crime type.

&nbsp;

<a id='results'></a>

## Project Trajectory, Results, and Interpretation

During the course of this project we had to shift our implementation multiple times given our EDA of the datasets.  Some datasets ended up being abandoned because they either had to much missing data that proved too difficult to impute or questionable data we did not trust for our analysis *(for example liquor license data)*.  We also decided that we needed to be able to associate spatial indicators to records of an underlying data set used to engineer our features (such as ``lat`` and ``lon``, neighborhood, zipcode, or census tract) because of the geospatial character of our analysis.

We also shifted what our desired final output of this project would be given time constraints.  We initially planned on having code in which a user could input a ``lat``, ``lon`` and other time (e.g. date and time of day) and weather conditions elements as input into the model to calculate probabilities of each type of crime occuring versus all others.  For this iteration we simply use each model developed to predict `crime-type` classes against our test data. 

The full analysis of the output of each model is discussed in detail in each individual model page.  Our best models have an ``accuracy score`` of around **0.35** on a multi-class categorization problem with nine different `crime-type` classes.  This is better than random chance so our predictors do have some degree of predictive power but not as high as our goals. We believe that the way the crimes are categorized and subset has a huge impact on accuracy.  On subsets of our data with fewer categories defined slightly differently we were able to achieve much higher accuracy scores as were summarized in our results above.  This is something we will explore much more deeply in future iterations of our predictive model to achieve accuracies and results more in line with our final objectives. The heavy spatial and temporal mixing of crime types across the City of Boston has proven to be a key challenge to address in the formalization of our model and research question.

Especially interesting are the relationships of specific `crime-type` classes to predictors such as ``bachelor-degree-or-more-perc``, ``commercial-mix-ratio``, ``industrial-mix-ratio``, ``tempavg``, or specific days of the week.  The interpretability graphs at the end of [the neural network model page](model-nn.md) as well as the lasso regularized coefficients plotted on our [logistic regression model page](model-logistic.md#coef), and the "top predictors" [illustrated for our decision tree-based models](model-trees.md) all show very interesting, yet varying, relationships between our predictors and each of the different `crime-type` classes.

We feel that our models show that it is possible to begin predicting the probability of different crime types in different areas of the City of Boston, albeit with lower than desired accuracy given the models and feature-set we currently have engineered. Overall, by redefining our problem statement and research questions to make them more specific we believe we may be able to achieve far more desireable accuracy in our predictions.  However, before operationalizing any resulting model for some specific use (perhaps by the City of Boston or other organizations), potential biases (e.g. racial or socio-economic) will need to be carefully evaluated in the results and actions will need to be taken to re-evaluate possible inputs to the model or clear guidance will need to be given on the specific methods used to interperet the model's output.  

&nbsp;

## Conclusions and Future Work 

Overall, we feel that our results show some promise and that further evaluation of how we subset our response classes and engineer our predictors will yield significant improvements in the predictive accuracy of our models.  In the future, we will explore further datasets to identify other features of use that may better separate among different types of crime.  We also still have [issues with multi-collinearity](data.md#correlation) in our existing predictor-set that will need to be addressed, with high priority, in the next iteration of our model.

We plan on further exploring each of the raw ``OFFENSE_CODE_GROUP`` values contained in the [underlying City of Boston crime incident reports dataset](data-crime.md) on top of which this analysis has been developed. And we will further investigate how they are distributed across each of our predictors.  This will help us understand which ``OFFENSE_CODE_GROUP`` values can be better differentiated by out predictors.  The present grouping of these code groups into our `crime-type` classes might be masking environmental influences on the original crime codes.  Our comparative subset class analyses were just the beginning of our exploration of how the categorization of crime types affect our models.

Finally, as described in the second paragraph [of our "results" section above](#results), we will be begin working out the code required for a user to input a ``lat``, ``lon`` and other time (e.g. date and time of day) and weather conditions elements to generate the resulting `crime-type` prediction statistics for those specific inputs to better understand the generalization and extensibility of our resulting models.
