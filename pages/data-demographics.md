---
title: "City of Boston Neighborhood Demographics EDA"
---

## Source materials 

Here is a list with links to the jupyter notebook and original dataset used to generate the findings on this page:

- [The neighborhood demographics notebook can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/015_EDA_neighborhood_demographics.ipynb)

- [The original City of Boston demographics data can be found online here.](https://data.boston.gov/dataset/neighborhood-demographics)

## Summary and challenges

By Boston neighborhood we have successfully pulled together demographic data in the following categories:
- Age 
- Housing Tenure
- Household Income
- Poverty Rate
- Educational Attainment/School Enrollment

For our **17 identified neighborhoods** we have created one master data frame including over **70 features** granting us flexibility for model experimentation. 

> Given that the demographics data is at an aggregated neighborhood level *(rather than by census tract)* further discussion is needed around model implementation.  
