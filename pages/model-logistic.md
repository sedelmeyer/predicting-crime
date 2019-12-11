---
title: "Logistic regression classification models"
---

[The notebook used to develop this baseline model can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/024_MODEL_logistic_classifiers.ipynb)

# Summary

Following the creation of our inital baseline model, [as described and interpreted on this page](model-baseline.md), where we used logistic regression with only `lat` and `lon` as our predictors, we then expanded our model to our entire feature-set for predictiing `crime-type` classes for each crime record. This page describes these additional logistic regression classifier modeling efforts and provide an interpretation of the results. For a full predictor-by-predictor listing of the predictors used in the models on this page, along with a brief description of each predictor, [please see this section of our "Models" page](models.md#predictors). used to conduct this 

Following the initial models below, we have also chosen to test a comparable set of logistic regression models, wherein we seek to predict a smaller subset of `crime-type` classes in an attempt to overcome some of our class imbalance challenges and to better understand the effect of reduced class categories on our model. [A detailed listing of the full set of `crime-type` response classes can be found here](models.md#response), and the [a description of the comparative secondary set of reduced classes can be found here](models.md#response-comp). 

# Model 1: Logistic regression classifier without regularization

### Model 1 parameters

For the initial model that we investigate on this page, we train a logistic regression classifier without regularization, as a point of comparison with [our initial baseline model](model-baseline.md). Once again, we trained two versions of our model, one without any class weighting applied to the model, and a second with "balanced" class weightings applied.

The parameters of the two scikit-learn `LogisticRegression` model objects fitted for our baseline model are:

**MODEL 1.a: Without balanced class weights**

```py
LogisticRegression(C=100000, class_weight=None, dual=False,
                   fit_intercept=True, intercept_scaling=1,
                   l1_ratio=None, max_iter=1000,
                   multi_class='multinomial', n_jobs=None,
                   penalty='l2', random_state=20, solver='lbfgs',
                   tol=0.0001, verbose=0, warm_start=False)
```

**MODEL 1.b: With balanced class weights**

```py
LogisticRegression(C=100000, class_weight=None, dual=False,
                   fit_intercept=True, intercept_scaling=1,
                   l1_ratio=None, max_iter=1000,
                   multi_class='multinomial', n_jobs=None,
                   penalty='l2', random_state=20, solver='lbfgs',
                   tol=0.0001, verbose=0, warm_start=False)

```

### Model 1 accuracy and AUC

Ultimately, these models resulted in the following training accuracies and average AUCs. As we can see the Model 1.a. generated without using balanced class weights acheived only a TEST accuracy of 0.2965, a 2 point improvement over the 0.2733 achieved with our baseline model. What this indicates to us is that, with our entire predictor set (versus using just `lat` and `lon` in our baseline model), the logistic regression classifier can more easily separate out `crime-type` classes in its prediction. Rather than using geo-spatial coodinates, two dimensions on which our `crime-type` classes are heavily mixed and difficult to separate in a linear manner, we now have a large set of additional dimensions on which to evaluate each crime record. This appears to have improved the predictive strength of our model. 

Another characteristic to note is that our TEST AUC has been even more strongly improved than our accuracy. Whereas in our baseline model our unweighted TEST AUC was 0.537, with all of our predictors added, our Model 1.a. achieves a TEST AUC of 0.617, a clear improvement.

Most notable in the results below are those that we achieve in Model 1.b, where we applied "balanced" class weightings while fitting our model. As can be seen below, our Model 1.b. prediction accuracy was 0.2131, much improved over the 0.1331 acheived in our balanced baseline model. Once again here, as we saw with our baseline models, the TEST AUC is once again comparable between our balanced and unbalanced models, indicating that the AUC metric suffers much less so than accuracy when balancing our our class weights.

**MODEL 1.a: Without balanced class weights**

```
This model resulted in the following accuracy:

Training	0.2965
Test		0.2977

The model AUC is:

		    weighted    unweighted
Training	0.6264		0.6221
Test		0.6235		0.6171
```

**MODEL 1.b: With balanced class weights**
```
This model resulted in the following accuracy:

Training	0.2131
Test		0.2131

The model AUC is:

		weighted	unweighted
Training	0.6246		0.6205
Test		0.6215		0.6152
```





As an initial baseline model, we ran several multi-class Logistic Regression models on a version of our predictors outlined below, in which all non-binary predictors were standardized to adjust for variability in scale among predictors. Variations attempted while building our baseline model included both one-vs-rest and multinomial versions of the model. In addition, we ran the versions of the models without regularization and then with L1 Lasso-like regularization (but without cross-validation) to ultimately examine coefficient shrinkage and to begin understanding relationships between our response classes and each individual predictor. For reference, the best baseline model reported here was specified with the following parameters::

```py
LogisticRegression(C=1, class_weight=None, dual=False,    
                   fit_intercept=True, intercept_scaling=1, 
                   l1_ratio=None, max_iter=10000, 
                   multi_class='multinomial', n_jobs=None, 
                   penalty='l1',random_state=20, solver='saga', 
                   tol=0.0001, verbose=0, warm_start=False)
```

## Predictors

Listed below are the predictors used in our baseline model. Additional predictors still under development for future iterations of our model are listed separately in Appendix 1 of this document.

1. **Day of week**
- This is a one-hot-encoded categorical variable for Tue, Wed, Thu, Fri, Sat, and Sun, indicating the day of the week during which the incident occurred.

2. **Month of year**
- This is a one-hot-encoded categorical variable for Feb, Mar, Apr, May, Jun, Jul, Aug, Sep, Oct, Nov, and Dec indicating the month of the incident.

3. **Night**
- This is a binary variable indicating whether the crime occurred between the hours of 8pm and 4am.
- The next iteration of this model will use actual sunset/sunrise times (as recorded by local NOAA weather
stations) for the date the incident occurred to specify this predictor.

1. **Median residential property value**
    - This provides the annual median property value for all residential properties in each census tract.

2. **Median residential value, 3-year CAGR**
    - This provides a measure of gentrification/development trend activity in the observation’s census tract area and year of occurrence.

3. **Median residential property value Gini coefficient**
    - This feature is used to measure "disparity" or inequality of median residential property values within each census tract.

4. **Median residential property value Gini coefficient, 3-year CAGE**
    - This provides a measure of growing or shrinking inequality in the observation’s census tract area and year of occurrence.

5. **Commercial properties mix ratio**
    - This provides a measure as to how “commercial” the corresponding census tract is each year, as measured by total assessed commercial property value in the tract divided by the total assessed value for all property in the tract during the given observation year.

6. **Commercial properties mix ratio, 3-year CAGR**
    - This provides a measure of how much more or less commercial the tract is becoming at the time of the observation.

7. **Industrial properties mix ratio**
    - This provides a measure as to how “industrial” the corresponding census tract is, as measured by total assessed industrial property value in the tract divided by the total assessed value for all property in the tract during the given observation year.

8. **Industrial properties mix ratio, 3-year CAGR**
    - This provides a measure of how much more or less industrial the tract is becoming at the time of the observation.

9. **Owner-occupied residential property ratio**
    - This is the proportion of the residential and mixed-use properties that are owner-occupied in each census tract during each given observation year.
    - To a degree this acts as a measure of local ownership as well as a potential indicator of absentee property ownership at the census tract-level.

10. **Owner-occupied residential property ratio, 3-year CAGR**
    - Measures trend changes in local ownership for the census tract at the time of observation.

## Model results

While we still have some issues with missingness and collinearity in several of our features (collinearity information is included in Appendix 2) to resolve in future iterations of our predictive model, our best baseline model, which used lasso regularized logistic regression with multinomial classification, resulted in a training accuracy score of 0.2733 and TEST score of 0.2730. Given the geographical inter-mixing of our response classes and the high bias of these results, we suspect that the linear decision boundaries of a logistic function are not expressive enough for accurately defining ourfeature space and predicting results. For that reason, we expect to see better accuracy results in future iterations of the model wherein we plan to first use non-parametric methods such as k-Nearest Neighbors and Decision Tree ensembles, and then later Artificial Neural Networks trained on our soon to be expanded feature set.

Even if a logistic function does not provide sufficient expressiveness for our classification problem, it does provide the benefit of interpretable results, from which we can begin to develop a better understanding of the relationships between specific predictors and response classes. For an overview of our estimated coefficients (as well as an indication of which predictors are found to be “not important” via lasso coefficient shrinkage to zero for certain response classes), please see the figures provided in Appendix 3.

![lasso-regularized-coefficients]({{ site.url }}/figures/model-baseline/base-model-lasso-coefficient-estimates.png)