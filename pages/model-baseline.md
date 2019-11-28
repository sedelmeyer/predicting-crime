---
title: "Baseline model using logistic regression"
---

The notebook used to develop this baseline model can be found at:

[https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/021_MODEL_baseline_logistic_classifier.ipynb](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/021_MODEL_baseline_logistic_classifier.ipynb)

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

4. **Median residential property value**
- This is measured by census tract area in which and year when the observation occurred.

5. **Median residential value, 3-year CAGR**
- This provides a measure of gentrification/development trend activity in the observation’s census tract area
and year of occurrence.

6. Disparity of residential property values (Gini coefficient)
○ For this feature “disparity” is measured using the Gini coefficient as a measure of economic inequality in
the observation’s census tract and year.
7. Disparity change trend for residential property values (Gini 3-year CAGR)
○ This provides a measure of growing or shrinking inequality in the observation’s census tract area and year
of occurrence.
8. Commercial properties mix ratio
○ This provides a measure as to how “commercial” the corresponding census tract is, as measured by total
assessed commercial property value in the tract divided by the total assessed value for all property in the
tract during the given observation year.
9. Commercial properties mix ratio, 3-year CAGR
○ Provides a measure of how much more or less commercial the tract is becoming at the time of the
observation.
10. Industrial properties mix ratio
○ This provides a measure as to how “industrial” the corresponding census tract is, as measured by total
assessed industrial property value in the tract divided by the total assessed value for all property in the
tract during the given observation year.
11. Industrial properties mix ratio, 3-year CAGR
○ Provides a measure of how much more or less industrial the tract is becoming at the time of the
observation.
12. Owner-occupied residential property ratio
○ What proportion of the residential and mixed-use properties are owner-occupied in the corresponding
census tract during the given observation year.
○ To a degree this acts as a measure of local ownership as well as a potential indicator of absentee
property ownership.
13. Owner-occupied residential property ratio, 3-year CAGR
○ Measures trend changes in local ownership for the census tract at the time of observation.

## Model results

While we still have some issues with missingness and collinearity in several of our features (collinearity information is included in Appendix 2) to resolve in future iterations of our predictive model, our best baseline model, which used lasso regularized logistic regression with multinomial classification, resulted in a training accuracy score of 0.2733 and TEST score of 0.2730. Given the geographical inter-mixing of our response classes and the high bias of these results, we suspect that the linear decision boundaries of a logistic function are not expressive enough for accurately defining ourfeature space and predicting results. For that reason, we expect to see better accuracy results in future iterations of the model wherein we plan to first use non-parametric methods such as k-Nearest Neighbors and Decision Tree ensembles, and then later Artificial Neural Networks trained on our soon to be expanded feature set.

Even if a logistic function does not provide sufficient expressiveness for our classification problem, it does provide the benefit of interpretable results, from which we can begin to develop a better understanding of the relationships between specific predictors and response classes. For an overview of our estimated coefficients (as well as an indication of which predictors are found to be “not important” via lasso coefficient shrinkage to zero for certain response classes), please see the figures provided in Appendix 3.

![lasso-regularized-coefficients]({{ site.url }}/figures/model-baseline/base-model-lasso-coefficient-estimates.png)