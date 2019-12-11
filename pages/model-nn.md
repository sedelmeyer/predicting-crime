---
title: "Modeling using Decision Trees"
---

[The Neural Networks notebook can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/030_model_NN.ipynb)

[The NN Interpretation notebook can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/035_NN_interpretability.ipynb)

After exploring various kind of interpretable models, we turn to the dark side and fit a powerful Neural Network using Keras to learn as much as we can from the data, and then use its predictions to draw inferences.

# Neural Network basic model

We start with a simple 3-layer fully connected Neural Network with 64 nodes per layer, without relu activation and a simple SGD optimizer. 

- The only real improvement we make is weighting the classes based on the number of occourrences of each class to account for unbalances in the Crime dataset.

- Also, remember to use the scaled version of the dataset, as Neural Networks are sensitive to variation in magnitude between features.

- Training for 10 epochs and a batch size of 32 is enough for close to optimal performance, for a super-fast training time of 3 mins.

![model_1]({{ site.url }}/figures/model-nn/model1.PNG)

- **Performance**: excellent on the training set (0.6482 weighted AUC), poor on the test set (0.4981 wAUC, worse than chance).

