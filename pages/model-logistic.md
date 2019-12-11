---
title: "Logistic regression classification models"
---

[The notebook used to develop this baseline model can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/024_MODEL_logistic_classifiers.ipynb)

# Summary

Following the creation of our inital baseline model, [as described and interpreted on this page](model-baseline.md), where we used logistic regression with only `lat` and `lon` as our predictors, we then expanded our model to our entire feature-set for predictiing `crime-type` classes for each crime record. This page describes these additional logistic regression classifier modeling efforts and provide an interpretation of the results. For a full predictor-by-predictor listing of the predictors used in the models on this page, along with a brief description of each predictor, [please see this section of our "Models" page](models.md#predictors). used to conduct this 

Following the initial models below, we have also chosen to test a comparable set of logistic regression models, wherein we seek to predict a smaller subset of `crime-type` classes in an attempt to overcome some of our class imbalance challenges and to better understand the effect of reduced class categories on our model. [A detailed listing of the full set of `crime-type` response classes can be found here](models.md#response), and the [a description of the comparative secondary set of reduced classes can be found here](models.md#response-comp). 

# Model 1: Logistic regression classifier without regularization

# Model 1 parameters

For the initial model that we investigate on this page, we train a logistic regression classifier without regularization, as a point of comparison with [our initial baseline model](model-baseline.md). Once again, we trained two versions of our model, one without any class weighting applied to the model, and a second with "balanced" class weightings applied.

The parameters of the two scikit-learn `LogisticRegression` model objects fitted for our baseline model are:

**MODEL 1.a.: Without balanced class weights**

```py
LogisticRegression(C=100000, class_weight=None, dual=False,
                   fit_intercept=True, intercept_scaling=1,
                   l1_ratio=None, max_iter=1000,
                   multi_class='multinomial', n_jobs=None,
                   penalty='l2', random_state=20, solver='lbfgs',
                   tol=0.0001, verbose=0, warm_start=False)
```

**MODEL 1.b.: With balanced class weights**

```py
LogisticRegression(C=100000, class_weight=None, dual=False,
                   fit_intercept=True, intercept_scaling=1,
                   l1_ratio=None, max_iter=1000,
                   multi_class='multinomial', n_jobs=None,
                   penalty='l2', random_state=20, solver='lbfgs',
                   tol=0.0001, verbose=0, warm_start=False)

```

# Model 1 accuracy and AUC

Ultimately, these models resulted in the following training accuracies and average AUCs. As we can see the Model 1.a. generated without using balanced class weights acheived only a TEST accuracy of 0.2965, a 2 point improvement over the 0.2733 achieved with our baseline model. What this indicates to us is that, with our entire predictor set (versus using just `lat` and `lon` in our baseline model), the logistic regression classifier can more easily separate out `crime-type` classes in its prediction. Rather than using geo-spatial coodinates, two dimensions on which our `crime-type` classes are heavily mixed and difficult to separate in a linear manner, we now have a large set of additional dimensions on which to evaluate each crime record. This appears to have improved the predictive strength of our model. 

Another characteristic to note is that our TEST AUC has been even more strongly improved than our accuracy. Whereas in our baseline model our unweighted TEST AUC was 0.537, with all of our predictors added, our Model 1.a. achieves a TEST AUC of 0.617, a clear improvement.

Most notable in the results below are those that we achieve in Model 1.b, where we applied "balanced" class weightings while fitting our model. As can be seen below, our Model 1.b. prediction accuracy was 0.2131, much improved over the 0.1331 acheived in our balanced baseline model. Once again here, as we saw with our baseline models, the TEST AUC is once again comparable between our balanced and unbalanced models, indicating that the AUC metric suffers much less so than accuracy when balancing our our class weights.

**MODEL 1.a.: Without balanced class weights**

```
This model resulted in the following accuracy:

Training	0.2965
Test		0.2977

The model AUC is:

		weighted    unweighted
Training	0.6264		0.6221
Test		0.6235		0.6171
```

**MODEL 1.b.: With balanced class weights**
```
This model resulted in the following accuracy:

Training	0.2131
Test		0.2131

The model AUC is:

		weighted	unweighted
Training	0.6246		0.6205
Test		0.6215		0.6152
```

# Model 1 predictions

By viewing the number of predictions generated by each version of the Model 1, we can see that, [unlike our baseline model without class weighting](model-baseline.md#predict), with our full predictor-set our new Model 1.a. generates predictions for almost all of our `crime-type` response classes. The only exception, visible in the first table below, is `crime-type` class 5 (`robbery`) which also happens to represent the `crime-type` class with the lowest proportion of true observations among all of our `crime-type` classes [as was shown in the response variable summary table on our "Models" page](models.md#response). And, as we'd expect Model 1.b. with balanced class weighting generates predictions for all of our `crime-type` response classes, including class 5. These results, particularly for Model 1.a., indicate to us that our full set of predictors does a good job at beginning to separate response classes for the model, even with the severe class imbalances in our training set.  

**MODEL 1.a.: Without balanced class weights**
```
The number of classes predicted by class are:

TRAINING
       count  proportion
class                   
0         37    0.000288
1         10    0.000078
2       6376    0.049676
3         33    0.000257
4      39613    0.308628
6      73599    0.573415
7         48    0.000374
8       8636    0.067284

TEST
       count  proportion
class                   
0          3    0.000093
1          2    0.000062
2       1608    0.050112
3          8    0.000249
4       9897    0.308433
6      18453    0.575075
7         13    0.000405
8       2104    0.065570
```

**MODEL 1.b.: With balanced class weights**

```
The number of classes predicted by class are:

TRAINING
       count  proportion
class                   
0      15715    0.122437
1      13780    0.107361
2      24808    0.193281
3       6607    0.051476
4      33843    0.263673
5       8895    0.069302
6      17494    0.136297
7       5388    0.041978
8       1822    0.014195

TEST
       count  proportion
class                   
0       3788    0.118050
1       3487    0.108670
2       6214    0.193655
3       1624    0.050611
4       8525    0.265676
5       2242    0.069870
6       4386    0.136687
7       1373    0.042789
8        449    0.013993
```

Now, rather than to conduct a detailed breakdown of our confusion matrices and confusion matrix derived classification metrics [as we did on our baseline model page](model-baseline.md#confmat), we will instead jump right to the receiver operator characteristics curves for the best performing version of our Model 1 (Model 1.a.), allowing us to get more quickly to our next logistic regression classifier models. 

## BEWARE: CONTENT BELOW HAS NOT YET BEEN UPDATED

# Model 1 receiver operator characteristic (ROC) curves by model and class

As was discussed in [our analysis of our baseline model's ROC curves](model-baseline.md#roc), we are hoping to see curves for each class that rise very steeply toward a true positive rate (TPR) of 1.0 at very low values for the corresponding false positive rates (FPR), idealing forming a very high, far left, sharp elbow in each curve. While our Model 1.a. ROC curves do not exemplify those visual characteristic, they are visually far improved over the curves we saw in our baseline model [as per the reasons described there](model-baseline.md#roc).

Shown in the plots below, we can see that our Model 1.a. ROC curves have all begun to bow upward and away from the dashed reference line at which AUC would be equal to 0.50. While some `crime-type` class ROC curves appear to be more favorable than others, `drugs-substances`, `harassment-disturbance`, and `theft` stand out as exhibiting the best properties. Overall, the class-by-class shapes of these curves support what we would expect to see with the improved 0.62 average TEST AUC, which improved over the 0.54 generated by our baseline model. 

![roc]({{ site.url }}/figures/model-logistic/roc-all.png)

![roc-class]({{ site.url }}/figures/model-logistic/roc-by-class-all.png)


# Model 2: Logistic regression classifier with cross-validated lasso (l1) regularization

**MODEL 2: Without balanced class weights**

```py
LogisticRegressionCV(Cs=10, class_weight='balanced',
                     cv=None, dual=False, fit_intercept=True, intercept_scaling=1.0, l1_ratios=None,
                     max_iter=1000, multi_class='multinomial',
                     n_jobs=None, penalty='l1', random_state=20,
                     refit=True, scoring='roc_auc_ovr',
                     solver='saga', tol=0.0001, verbose=0)
```

**MODEL 2: With balanced class weights**

```
This model resulted in the following accuracy:

Training	0.2133
Test		0.2133

The model AUC is:

		weighted	unweighted
Training	0.6246		0.6205
Test		0.6215		0.6152
```

**MODEL 2: With balanced class weights**
```
The number of classes predicted by class are:

TRAINING
       count  proportion
class                   
0      15749    0.122702
1      13831    0.107758
2      24818    0.193359
3       6490    0.050564
4      34083    0.265543
5       8829    0.068787
6      17477    0.136165
7       5292    0.041230
8       1783    0.013891

TEST
       count  proportion
class                   
0       3800    0.118424
1       3494    0.108888
2       6221    0.193873
3       1585    0.049395
4       8575    0.267234
5       2223    0.069278
6       4396    0.136998
7       1351    0.042103
8        443    0.013806
```

**MODEL 2: With balanced class weights**
```
The resulting confusion matrix:

TEST
Actual        0     1     2     3     4    5     6     7     8  Total
Predicted                                                            
0           378   129   351   261   498  108   982   367   726   3800
1           160   280   275   354   542   66   920   432   465   3494
2           240   248  1269   433   803  184  1558   590   896   6221
3            70    65   150   182   226   39   448   176   229   1585
4           340   344   693   527  2201  220  1661   987  1602   8575
5            99   128   179   154   344  100   515   258   446   2223
6           205   128   235   388   294   80  2129   359   578   4396
7            71    75    94    74   214   44   314   201   264   1351
8            17    19    25    24    70   15   112    57   104    443
Total      1580  1416  3271  2397  5192  856  8639  3427  5310  32088

The classification metrics derived from the confusion matrix are:

TEST
         TP    FP    FN     TN    TPR    FNR    FPR    TNR
class                                                                 
0       378  3422  1202  27086  0.239  0.761  0.112  0.888
1       280  3214  1136  27458  0.198  0.802  0.105  0.895
2      1269  4952  2002  23865  0.388  0.612  0.172  0.828
3       182  1403  2215  28288  0.076  0.924  0.047  0.953
4      2201  6374  2991  20522  0.424  0.576  0.237  0.763
5       100  2123   756  29109  0.117  0.883  0.068  0.932
6      2129  2267  6510  21182  0.246  0.754  0.097  0.903
7       201  1150  3226  27511  0.059  0.941  0.040  0.960
8       104   339  5206  26439  0.020  0.980  0.013  0.987

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