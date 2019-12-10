---
title: "Modeling using Decision Trees"
---

[The Decision Tree notebook can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/031_MODEL_decision_trees.ipynb)

After exploring the baseline model we explored a Decision Tree Classifier model. The Decision Tree model with tuning does a fair job with the data and reaches a max accuracy of approximately 0.35 with nine classes of crime (this is similar to our our models).


# Decision Tree Model

![trees_dif_depths]({{ site.url }}/figures/model-trees/trees_dif_depths.PNG)



**Top Predictors** 
![tree_plot]({{ site.url }}/figures/model-trees/tree_plot.PNG)
![tree_top_predictors]({{ site.url }}/figures/model-trees/tree_top_predictors.PNG)


# Overfitting

Accuracy of overfit tree model (Train): 0.887855272999252
Accuracy of overfit tree model (Test):  0.29216529543754677

# Bagging
Using 55 trees:
Accuracy of bagging model (Train):  0.0487175891298928
Accuracy of bagging Model (Test):  0.04724507604088756

# Bootstraps Affects & Bagging Ensemble's Performance
![bootstrap_accuracy]({{ site.url }}/figures/model-trees/bootstrap_accuracy.PNG)



# Random Forest
Accuracy of random forest model (Train):  0.4243954126153079
Accuracy of random forest model (Test):  0.350068561455996

Random forest randomly selects a subset of predictors to split on. Therefore the first split can vary based on what subset of predictors is being used. Bagging does not subset the predictors so is always using the same best predictor.

Random forest can possibly capture more variance in the data because it is aggregating trees that are more varied. Theoretically random forest should therefore be able to get higher accuracies than bagging.
***Accuracy Comparison:***
![accuracy_comparison]({{ site.url }}/figures/model-trees/accuracy_comparison.PNG)

# Boosting
ADA Boost Classifier
![ada_boost_3]({{ site.url }}/figures/model-trees/ada_boost_3.PNG)
![ada_boost_5]({{ site.url }}/figures/model-trees/ada_boost_5.PNG)
![ada_boost_6]({{ site.url }}/figures/model-trees/ada_boost_6.PNG)
![ada_boost_7]({{ site.url }}/figures/model-trees/ada_boost_7.PNG)
![ada_boost_8]({{ site.url }}/figures/model-trees/ada_boost_8.PNG)



# Best Model: Random Forest Results

***Confusion matrices***
![confusion_matrix_rf]({{ site.url }}/figures/model-trees/confusion_matrix_rf.PNG)
![confusion_matrix_rf_2]({{ site.url }}/figures/model-trees/confusion_matrix_rf_2.PNG)
***AUC***
![roc_auc]({{ site.url }}/figures/model-trees/roc_auc.PNG)