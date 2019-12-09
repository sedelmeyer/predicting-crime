---
title: "Modeling using KNN Classifier"
---

[The notebook used to develop this baseline model can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/025_MODEL_knn.ipynb)

As an initial baseline model, we ran several multi-class Logistic Regression models on a version of our predictors outlined below, in which all non-binary predictors were standardized to adjust for variability in scale among predictors. Variations attempted while building our baseline model included both one-vs-rest and multinomial versions of the model. In addition, we ran the versions of the models without regularization and then with L1 Lasso-like regularization (but without cross-validation) to ultimately examine coefficient shrinkage and to begin understanding relationships between our response classes and each individual predictor. For reference, the best baseline model reported here was specified with the following parameters::

```py
KNeighborsClassifier(algorithm='auto', leaf_size=30,
					 metric='minkowski',metric_params=None, n_jobs=-1, 
					 n_neighbors=205, p=1, weights='distance'),
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

6. **Disparity of residential property values (Gini coefficient)**
- For this feature “disparity” is measured using the Gini coefficient as a measure of economic inequality in
the observation’s census tract and year.

7. **Disparity change trend for residential property values (Gini 3-year CAGR)**
- This provides a measure of growing or shrinking inequality in the observation’s census tract area and year
of occurrence.

8. **Commercial properties mix ratio**
- This provides a measure as to how “commercial” the corresponding census tract is, as measured by total
assessed commercial property value in the tract divided by the total assessed value for all property in the
tract during the given observation year.

9. **Commercial properties mix ratio, 3-year CAGR**
- Provides a measure of how much more or less commercial the tract is becoming at the time of the
observation.

10. **Industrial properties mix ratio**
- This provides a measure as to how “industrial” the corresponding census tract is, as measured by total
assessed industrial property value in the tract divided by the total assessed value for all property in the
tract during the given observation year.

11. **Industrial properties mix ratio, 3-year CAGR**
- Provides a measure of how much more or less industrial the tract is becoming at the time of the
observation.

12. **Owner-occupied residential property ratio**
- What proportion of the residential and mixed-use properties are owner-occupied in the corresponding
census tract during the given observation year.
- To a degree this acts as a measure of local ownership as well as a potential indicator of absentee
property ownership.

13. **Owner-occupied residential property ratio, 3-year CAGR**
- Measures trend changes in local ownership for the census tract at the time of observation.

## Model tuning

> *Given the large size of our dataset, 10% of the data was used to tune the parameters for the model.*  

The major parameters we tuned for the KNN Classifier were **weights** and **p**.

**Model 1** was run with the default KNN parameters and reached a max accuracy of 0.317 at a k_value of 145.

![knn_accuracy_model-01]({{ site.url }}/figures/model-knn/knn_accuracy_model-01.png)

**Model 2** was run with p=1 (Manhattan distance) which resulted in a very similar max accuracy of  0.316 at a k_value of 85.

![knn_accuracy_model-02]({{ site.url }}/figures/model-knn/knn_accuracy_model-02.png)

**Model 3** was run with weights='distance' and p=1 (Manhattan distance) which resulted in a very similar max accuracy of  0.317 at a k_value of 205 *(but the accuracy was still climbing)*.

![knn_accuracy_model-03]({{ site.url }}/figures/model-knn/knn_accuracy_model-03.png)


## Model results
We then took our best knn model (wieights='distance' and p=1) and ran it on the full dataset.  The curve flattens out as k increases with an asymptote around 0.355.  The elbow of the curve is around a k value of 100.  And the curve really flattens out beyond a k value of around 200.  To maximize predictability we will use a **k value of 205** below.

![knn_kval_full-test-data]({{ site.url }}/figures/model-knn/knn_kval_full-test-data.png)

The selected KNN model reaches an accuracy of **0.346** on the test dataset.  Below we will explore the predictions in detail using accuracy scores, confusion matrix and auc curves.

The predictions of the model in both train and test were distributed across the crimes which is a good sign *(an accuracy of 0.27 can be achieved by predicting everything is a theft).*

![knn_predictions_train]({{ site.url }}/figures/model-knn/knn_predictions_train.png)
![knn_predictions_test]({{ site.url }}/figures/model-knn/knn_predictions_test.png)

The confusion matrix and metrics based on the confusion matrix show how the KNN model performed for each of the classes of crime.  The model appears to do especially well predicting class=2 (drug_substances).

![knn_confusion-matix]({{ site.url }}/figures/model-knn/knn_confusion-matix.png)
![knn_confusion-matix]({{ site.url }}/figures/model-knn/knn_confusion-matix.png)