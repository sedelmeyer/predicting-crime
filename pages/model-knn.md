---
title: "Modeling using KNN Classifier"
---

[The KNN notebook can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/025_MODEL_knn.ipynb)

After exploring the baseline model we explored a KNN Classifier model.  KNN models can be quite processor-intensive so model tuning was performed on a 10% sample of the dataset.  The best KNN model was then fit to the full dataset and analyzed.  The KNN model with tuning does a decent job with the data and reaches a max accuracy of approximately 0.35 with nine classes of crime *(this is similar to our our models)*.

KNN models are affected by the scale of the predictor so we used scaled data to train (``X_train_scaled`` and test (``X_test_scaled``).  A scaler (``X_scaler``) is included in our repo to convert the predictors to their original values.   

> KNN is not the best for determining top predictors *(please refer to our Logistic Regression and Decision Tree models for information on top predictors)*.

For reference, the best KNN model reported here was specified with the following parameters:
```py
KNeighborsClassifier(algorithm='auto', leaf_size=30, metric='minkowski', 
                     metric_params=None, n_jobs=-1, n_neighbors=205, p=1, 
                     weights='distance'),
```
## Model tuning

> *Given the large size of our dataset, 10% of the data was used to tune the parameters for the model.*  

The major parameters we tuned for the KNN Classifier were ``weights`` and ``p``.

**Model 1** was run with the default KNN parameters and reached a max accuracy of 0.317 at a ``k_value`` of 145.

![knn_accuracy_model-01]({{ site.url }}/figures/model-knn/knn_accuracy_model-01.png)

**Model 2** was run with p=1 (Manhattan distance) which resulted in a very similar max accuracy of  0.316 at a ``k_value`` of 85.

![knn_accuracy_model-02]({{ site.url }}/figures/model-knn/knn_accuracy_model-02.png)

**Model 3** was run with ``weights='distance'`` and ``p=1`` (Manhattan distance) which resulted in a very similar max accuracy of 0.317 at a ``k_value`` of 205 *(but the accuracy was still climbing)*.

![knn_accuracy_model-03]({{ site.url }}/figures/model-knn/knn_accuracy_model-03.png)


## Model results
We then took our best knn model (``weights='distance'`` and ``p=1``) and ran it on the full dataset.  The curve flattens out as k increases with an asymptote around 0.355.  The elbow of the curve is around a k value of 100.  And the curve really flattens out beyond a k value of around 200.  To maximize predictability we will use a **k value of 205** below.

![knn_kval_full-test-data]({{ site.url }}/figures/model-knn/knn_kval_full-test-data.png)

The selected KNN model reaches an accuracy of **0.346** on the test dataset.  Below we will explore the predictions in detail using accuracy scores, confusion matrix and auc curves.

The predictions of the model in both train and test were distributed across the crimes which is a good sign *(an accuracy of 0.27 can simply be achieved by predicting everything is a class=6 (theft)).*

![knn_predictions_train]({{ site.url }}/figures/model-knn/knn_predictions_train.png)

![knn_predictions_test]({{ site.url }}/figures/model-knn/knn_predictions_test.png)

The confusion matrix and metrics based on the confusion matrix show how the KNN model performed for each of the classes of crime.  The model appears to do especially well predicting **class=2 (drug_substances)** with a ``True Positive Rate (TPR)`` of **0.499**.

![knn_confusion-matix]({{ site.url }}/figures/model-knn/knn_confusion-matix.png)
![knn_confusion-matrix_calcs]({{ site.url }}/figures/model-knn/knn_confusion-matrix_calcs.png)

We had to make some modifications to allow AUC scores to be calculated for multi-class predictions *(requires 0.22 version of sklearn)*.    The KNN model achieved an ``AUC Average`` of **0.653** and an ``Weighted AUC Average`` of **0.661**. 

The AUC curves below confirm what we saw in the confusion matrix that the model is especially good at predicting **class=2 (drug_substances)**.  

![knn_auc-curves_combined]({{ site.url }}/figures/model-knn/knn_auc-curves_combined.png)

![knn_auc-curves_individual]({{ site.url }}/figures/model-knn/knn_auc-curves_individual.png)

## Different Subsets of the Data
[The KNN subset data notebook can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/025_MODEL_knn_subset.ipynb)

We are using the full crime dataset along with customized categories that we created.  How the data is subset and how the categories are chosen can greatly impact the accuracy our models achieve.  Our framework is extensible enough to accommodate for different subsets and categories based on requirements.  

For example below are the results for a KNN model run on a subset of the data with three classes:
**(drugs-substances, theft, violence-aggression)**

> **Much better model scores:**  
Accuracy 0.346 --> 0.603, 
AUC 0.653 --> 0.756, 
Weighted AUC 0.661 --> 0.741

``Testing Accuracy`` = **0.603**

``AUC Average`` = **0.756**

``Weighted AUC Average`` = **0.741**

![knn-subset_confusion-matix]({{ site.url }}/figures/model-knn/knn-subset_confusion-matix.png)

![knn-subset_confusion-matrix_calcs]({{ site.url }}/figures/model-knn/knn-subset_confusion-matrix_calcs.png)

![knn-subset_auc-curves_combined]({{ site.url }}/figures/model-knn/knn-subset_auc-curves_combined.png)
