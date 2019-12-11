---
title: "Models"
---

A number of different model types were tested during the development of this predictive analysis:

For a summary of our final results, achieved with the best of our tested models, please see the Results page.

For a look into the types of models we developed prior to reaching those results, please see the following model pages:

1. [Baseline Logistic Regression Classification Model](model-baseline.md)
2. [Logistic Regression Classification Models](model-logistic.md)
3. [k-Nearest Neighbors (kNN) Classifier Models](model-knn.md)
4. [Decision Tree Classifiers and Ensemble Methods](model-trees.md)
5. Feed Forward Artificial Neural Network (i.e. multi-level perceptron) **(TBD)**

# About the response variable we are predicting

The response variable for our model is ​**type of crime** defined as a set of 9 `crime-type` categories consolidated from a subset of the 66 available `OFFENSE_CODE_GROUP` categories in the [raw crime incidents dataset described here](data-crime.md) over the years 2016-2019. 

The 9 crime-type categories are:

```
class       class-name
0           other
1           burglary
2           drugs-substances
3           fraud
4           harassment-disturbance
5           robbery
6           theft
7           vandalism-property
8           violence-aggression
```

# Secondary comparative reduced number of response classes

Please note that we have also performed a secondary subsetting of `crime-type` classes in several of our prediction models. This was done as a comparative analysis to attempt to overcome the imbalanced classes existing in our primary set of `crime-type` classes and to examine potential changes in predictive accuracy when we subset for a smaller grouping of particularly meaningful classes.

The seconday subsetting of classes can be summarized as such:

```
class       class-name
0 	        drugs-substances
1 	        theft
2 	        violence-aggression
```

Just note that in this particular secondary grouping of classes, `violence-aggression` has been combined with `robbery` due to the physical nature of the crime and the increased risk/threat of violence that such a crime entails.

## Model predictors

Listed below are the full set of predictors used in our models. For an in-depth EDA of these predictors, or to view the original EDAs performed on the raw data sources from which these predictors were derived, [please see the "Data" page of this analysis.](data.md)

1. `lat` and `lon`
    - These are the latitude and longitude coordinates for each observed crime record.

1. `day-of-week`
    - This is a one-hot-encoded categorical variable split into the individual predictors `Tuesday`, `Wednesday`, `Thursday`, `Friday`, `Saturday`, and `Sunday`, indicating the day of the week during which the incident occurred.

1. `month-of-year`
    - This is a one-hot-encoded categorical variable split into the individual predictors `Feb`, `Mar`, `Apr`, `May`, `Jun`, `Jul`, `Aug`, `Sep`, `Oct`, `Nov`, and `Dec` indicating the month of the incident.

1. `night`
    - This is a binary variable indicating whether the crime occurred before sunrise or after sunset for the given day of the crime record.
    - Sunrise and sunset times were derived from NOAA daily local climatological data for the City of Boston.

1. `streetlights-night`
    - This is an interaction term measuring the number of streetlights within a 100 meter radius of each crime record that occured at night.
    - Daytime crime records are zero-valued for this predictor.

1. `tempavg`
    - This is the average dry bulb temperature in celcius for the City of Boston for the date on which each crime record occured.

1. `windavg`
    - This is the average daily windspeed in kilometers-per-hour in the City of Boston for the date on which each crime record occured.

1. `precip`
    - This is the amount of precipitation in inches that fell in the City of Boston for the date on which each crime record occured.

1. `snowfall`
    - This is the amount of snow in inches that fell in the City of Boston for the date on which each crime record occured.

1. `college-near`
    - This is a binary indicator identifying whether or not the crime occured within 500 meters of a college or university.

1. `highschool-near`
    - This is a binary indicator identifying whether or not the crime occured within 500 meters of a public or non-public highschool.

1. `median-age`
    - This is the median age of residents in the Boston neighborhood in which the crime record occured.

1. `median-income`
    - This is the median household income of residences in the Boston neighborhood in which the crime record occured.

1. `poverty-rate`
    - This is the proportion of residents living in poverty in the Boston neighborhood in which the crime record occured.

1. `less-than-high-school-perc`
    - This is the percentage of residents who achieved less than a highschool degree in the Boston neighborhood in which the crime record occured.

1. `bachelor-degree-or-more-perc`
    - This is the percentage of residents who attained a bachelor's degree or higher level of education in the Boston neighborhood in which the crime record occured.

1. `enrolled-college-perc`
    - This is the percentage of residents enrolled in college in the Boston neighborhood in which the crime record occured.

'commercial-mix-ratio', 'industrial-mix-ratio', 'owner-occupied-ratio',
   'residential-median-value', 'residential-gini-coef', 'commercial-mix-ratio-3yr-cagr',
   'industrial-mix-ratio-3yr-cagr', 'owner-occupied-ratio-3yr-cagr',
   'residential-gini-coef-3yr-cagr', 'residential-median-value-3yr-cagr'

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