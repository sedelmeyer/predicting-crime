---
title: "models"
---

A number of different model types were tested during the development of this predictive analysis:

For a summary of our final results, achieved with the best of our tested models, please see the Results page.

For a look into the types of models we developed prior to reaching those results, please see the following model pages:

1. [Baseline Logistic Regression Model](pages/model-baseline)
2. Cross-validated Logistic Regression Models (with added features) **(TBD)**
3. k-Nearest Neighbors (kNN) Classifier Models **(TBD)**
4. Decision Tree Classifiers and Ensemble Methods **(TBD)**
5. Feed Forward Artificial Neural Network (i.e. multi-level perceptron) **(TBD)**

## About the response variable we are predicting

The response variable for our model is ​**“type of crime,​"** defined as a set of 9 crime-type categories consolidated from a subset of the 66 available `OFFENSE_CODE_GROUP` categories in the [raw crime incidents dataset](pages/data-crime) over the years 2016-2019. The 9 crime-type categories are:

1. Burglary
2. Drugs-substances
3. Fraud
4. Harassment-disturbance
5. Robbery
6. Theft
7. Vandalism-property
8. Violence-aggression
9. Other