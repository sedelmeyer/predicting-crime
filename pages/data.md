---
title: "Data"
---

# Source materials

Here is a list with links to the jupyter notebook and original datasets used to generate the findings on this page:

- [The EDA notebook used to generate the below findings can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/023_EDA_training_data.ipynb) 

- [The notebook used to merge the engineered features examined in this EDA notebook can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/022_FEATURES_build_model_features.ipynb)

- [For a complete listing of all datasets and shapefiles examined and used in this analysis, please refer to the `data-inventory.csv` file located here.](https://github.com/sedelmeyer/predicting-crime/blob/master/data-inventory.csv)

# Raw data EDA, data cleansing, and feature engineering

To view the preliminary EDA findings and summaries of the feature engineering activities that were performed on the component datasets eventually merged into the model data examined on this page, please follow the links listed below. On each of those linked pages, you will also find links to the original source datasets used for each raw data EDA:

1. [Crime incident data](data-crime.md)
1. [Property assessment data](data-property.md)
1. [Streetlight location data](data-lights.md)
1. NOAA weather data
1. Neighborhood demographics data
1. Liquor licensing data
1. Public and non-public schools data
1. Universities and colleges data
1. Property violations
1. Various City of Boston shape files
    - These include Census tracts, Boston neighborhoods, Zip codes, Street segments, and Open spaces

# Introduction

This page outlines the comprehensive exploratory data analysis (EDA) conducted on the feature set engineered for our analysis. As is outlined above, a number of different data sources were investigated, cleansed, and enhanced in order to achieve the eventual feature set investigated on this page.

# Contents

The EDA outlined on this page follows this overall structure:

1. Description of the variable of interest we hope to measure
1. Description of the engineered features we have created
1. Geographic mappings of crime records for the City of Boston
1. Distributions of crime records by `crime-type` class among Boston neighborhoods and census tract areas
1. Investigation of the pair-wise relationships between each predictor and `crime-type` class
1. Investigation of distance-based predictors versus each `crime-type` class
1. Dimensionality reduction with principal component analysis (PCA) to evaluate explained variance among our predictors and the potential for effectively separating `crime-type` class predictions
1. Examination of pair-wise correlation among predictors and potential multi-collinearity

# Our variable of interest and number of overall records examined

Because our analysis seeks to predict, given any location in the City of Boston, the "type of crime" most likely to occur at that location, the response variable against which our analysis is built is `crime-type`.

This `crime-type` variable was derived from Crime Incident Records data maintained by the City of Boston, [and available online here](https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system). After our initial investigation of this data, [a summary of which can be found here](data-crime.md), we eventually subsetted the data to include all records containing corresponding geo-locational data recorded during the Jan. 2016 through Aug. 2019 period. In additional, we consolidated a subset of the 66 original crime type classes in the raw dataset down to a set of 9 remaining crime classes:

```
crime-type 	crime-type-name 	  crime-count
0 	        other 	                    6,321
1 	        burglary 	                5,664
2 	        drugs-substances 	       13,082
3 	        fraud 	                    9,587
4 	        harassment-disturbance 	   20,767
5 	        robbery 	                3,423
6 	        theft 	                   34,555
7 	        vandalism-property 	       13,710
8 	        violence-aggression 	   21,243
```

Once our data was subsetted, classes were filtered and consolidated, our final engineered features were merged with the crime incident data, and any records with missing data for any engineered features were removed, we were left with a dataset containing **160,440 observed crime records.**

Then, after performing our train set split with an 80/20 split, stratified by `crime-type`, our resulting training set (the data analyzed in this EDA) contained **128,352 training records.**

# Secondary subset of `crime-type` classes

Please note that we have also performed a secondary subsetting of `crime-type` classes in our subsequent [prediction models](models.md). This was done as a comparative analysis to attempt to overcome the imbalanced classes existing in our primary set of `crime-type` classes and to examine potential changes in predictive accuracy when we subset for a smaller grouping of particularly meaningful classes.

We mention this secondary subsetting of classes here primarily becuase this additional subset is examined via PCA in a later section of this EDA. The seconday subsetting of classes can be summarized as such:

```
crime-type 	crime-type-name 	  crime-count
0 	        drugs-substances 	       13,082
1 	        theft 	                   34,555
2 	        violence-aggression 	   24,666
```

Just note that in this particular grouping of classes, `violence-aggression` has been combined with `robbery` due to the physical nature of the crime and the increased risk/threat of violence that such a crime entails.

# Predictors used in this analysis

**ADD PREDICTORS HERE**

# Locational distributions of crime records

