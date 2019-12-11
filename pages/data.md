---
title: "Data"
---

# Source materials

Here is a list with links to the jupyter notebook and original datasets used to generate the findings on this page:

- [The EDA notebook used to generate the below findings can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/023_EDA_model_data.ipynb) 

- [The notebook used to merge the engineered features examined in this EDA notebook can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/022_FEATURES_build_model_features.ipynb)

- [For a complete listing of all datasets and shapefiles examined and used in this analysis, please refer to the `data-inventory.csv` file located here.](https://github.com/sedelmeyer/predicting-crime/blob/master/data-inventory.csv)

# Raw data EDA, data cleansing, and feature engineering

To view the preliminary EDA findings and summaries of the feature engineering activities that were performed on the component datasets eventually merged into the model data examined on this page, please follow the links listed below. On each of those linked pages, you will also find links to the original source datasets used for each raw data EDA:

1. [Crime incident data](data-crime.md)
1. [Property assessment data](data-property.md)
1. [Streetlight location data](data-lights.md)
1. NOAA weather data
1. [Neighborhood demographics data](data-demographics.md)
1. [Liquor licensing data](data-liquor.md)
1. [Educational institutions](data-education.md)
1. [Property violations](data-violations.md)
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
0 	        other                       6,321
1 	        burglary                    5,664
2 	        drugs-substances           13,082
3 	        fraud                       9,587
4 	        harassment-disturbance     20,767
5 	        robbery                     3,423
6 	        theft                      34,555
7 	        vandalism-property         13,710
8 	        violence-aggression        21,243
```

Once our data was subsetted, classes were filtered and consolidated, our final engineered features were merged with the crime incident data, and any records with missing data for any engineered features were removed, we were left with a dataset containing **160,440 observed crime records.**

Then, after performing our train set split with an 80/20 split, stratified by `crime-type`, our resulting training set (the data analyzed in this EDA) contained **128,352 training records.**

# Secondary subset of `crime-type` classes

Please note that we have also performed a secondary subsetting of `crime-type` classes in our subsequent [prediction models](models.md). This was done as a comparative analysis to attempt to overcome the imbalanced classes existing in our primary set of `crime-type` classes and to examine potential changes in predictive accuracy when we subset for a smaller grouping of particularly meaningful classes.

We mention this secondary subsetting of classes here primarily becuase this additional subset is examined via PCA in a later section of this EDA. The seconday subsetting of classes can be summarized as such:

```
crime-type 	crime-type-name 	   crime-count
0 	        drugs-substances            13,082
1 	        theft                       34,555
2 	        violence-aggression         24,666
```

Just note that in this particular grouping of classes, `violence-aggression` has been combined with `robbery` due to the physical nature of the crime and the increased risk/threat of violence that such a crime entails.

# Predictors used in this analysis

**ADD PREDICTORS HERE**

# Locational distributions of crime records

The plot below illustrates the distribution of crime records by each record's associated geo-location coordinates in the City of Boston. By color-coding each plotted location point according to its associated `crime-type` class, we can see that crime types demostrate heavy spatial mixing, with each of the different `crime-type` classes having occured in close proximity or overlapping one another over time from the year 2016 through 2019.

![crime-locs]({{ site.url }}/figures/features/crime-locs-all.png)

![crime-locs-by-type]({{ site.url }}/figures/features/crime-locs-all-by-type.png)

If we further subset our training records by Boston neighborhood, we can begin to examine bit more closely, whether this spatial mixing of classes might hold for all areas of the city, as well as how they might vary by particular neighborhood.

First, we can see that the greatest proportion of all total records occured in the Dorchester neighborhood, followed next by Roxbury, and then others.

![crime-by-hood]({{ site.url }}/figures/features/crime-by-neighborhood-barplot.png)

Examining this neighborhood-by-neighborhood breakdown a little more closely, we can see which particular neighborhoods experienced larger proportions of one `crime-type` versus another `crime-type` proportional each individual neighborhood's own crime incidents.

For example, in the plot below we can see that Back Bay experienced the highest proportion of `theft` among their own crime incidents when compared to other neighborhoods. The West End leads with the highest proportion of `violence-aggression` type crimes, whereas Beacon Hill has the lowest incidence of those crimes. And, Mattapan appears to lead with the highest in-neighborhood proportion of `harrassment-disturbance` incidents, while there are relatively very few in the Leather District.

![crime-by-hood-type]({{ site.url }}/figures/features/crime-by-neighborhood-and-type-barplot.png)

By looking at spatially mapped crime incidents in individual neighborhoods, we can also see a bit more clearly the overlapping nature of crime records by class. Starting with Dorchester, which we know to have the highest overall number of records, we can see just how densely mixed the crime incidents are.

![crime-dorchester]({{ site.url }}/figures/features/crime-locs-all-by-type-Dorchester.png)

And, looking at Jamaica Plain and East Boston, as they are plotted below, we can see visually how crimes are more heavily clustered in the more heavily populated areas of each neighborhood.

![crime-jamaica-plain]({{ site.url }}/figures/features/crime-locs-all-by-type-JamaicaPlain.png)

![crime-east-boston]({{ site.url }}/figures/features/crime-locs-all-by-type-EastBoston.png)

Even in Neighborhoods with a more sparse spatial distribution of crime records, we can still see evidence of heavy spatial mixing among `crime-type` classes.

![crime-north-end]({{ site.url }}/figures/features/crime-locs-all-by-type-NorthEnd.png)

![crime-w-roxbury]({{ site.url }}/figures/features/crime-locs-all-by-type-WestRoxbury.png)

**PRELIMINARY CONCLUSION:**

These observations suggest to us that purely locational predictors such as Latitude and Longitude alone will be insufficient for generating accurate predictions for each `crime-type` class.

# Locational change in crime records over time

As was discovered during [the initial EDA on the raw crime incidents records analysis](data-crime.md), to meaningfully plot choropleth distributions of crime records, we must do so with a sufficiently granular set of geographic areas. As is shown below, at the neighborhood level, the disproportionately high volume of crime records in Dorchester overwhelm the plotted distribution. However, this same level of aggregation presents a very different look when we consider the 4-year annual neighborhood-by-neighborhood change in proportion of crime records from 2016 to 2019 as is shown in the second plot below. There we can see that Dorchester is actually decreasing in overall proportion, while the South End, Roxbury, Downtown, South Boston, and Mattapan are all increasing.

![crime-hood-choro]({{ site.url }}/figures/features/crime-records-by-neighborhood.png)

![crime-hood-choro-4yr]({{ site.url }}/figures/features/crime-records-change-by-neighborhood.png)

Then, by plotting with a more granular shape area such as census tract, we can see much more specifically, with a set of smaller sub-regions, where the highest concentration of crime incidents have occured, as well as very specifically, where they are increasing the most.

![crime-tract-choro]({{ site.url }}/figures/features/crime-records-by-census%20tract.png)

![crime-tract-choro-4yr]({{ site.url }}/figures/features/crime-records-change-by-census%20tract.png)

Therefore, for the next set of plots we will use census tract areas for plotting aggregated summary statistics examining 4-year change in locational crime record proportions by `crime-type` class (for just a subset of our classes to preserve space), we will use census tracts as our level of aggregation.

Our first example shown below are `burglary` crime records. Here we can see that, while there are particular "hotspots" for burglaries represented in our dataset Downtown and in Allston, when we view the same records in respect to their 4-year change in propoprtions, a different set of locational relationships emerge, with the same Allston tract proportion dropping relatively heavily over time.

![crime-tract-burg]({{ site.url }}/figures/features/crime-records-by-census%20tract-burglary.png)

![crime-tract-burg-4yr]({{ site.url }}/figures/features/crime-records-change-by-census%20tract-burglary.png)

Next, looking at `drugs-substances` crime records, we can see a different distribution of hotspots overall, with particulaly high 4-year growth in the tract straddling the South Boston, South End, and Roxbury borders.

![crime-tract-drug]({{ site.url }}/figures/features/crime-records-by-census%20tract-drugs-substances.png)

![crime-tract-drug-4yr]({{ site.url }}/figures/features/crime-records-change-by-census%20tract-drugs-substances.png)

Then, when we look at `harassment-disturbance` records, another distribution emerges, more heavily distributed in tracts corresponding to Dorchester, Roxbury, Mattapan, and Hyde Park. In this case, the 4-year growth is most heavily focused in the Hyde Park tract bordering Mattapan, with Dorchester dropping most rapidly. 

![crime-tract-harass]({{ site.url }}/figures/features/crime-records-by-census%20tract-harassment-disturbance.png)

![crime-tract-harass-4yr]({{ site.url }}/figures/features/crime-records-change-by-census%20tract-harassment-disturbance.png)

To view similar plots for all `crime-type` classes, [please review the original notebook in which these plots were produced, which can be found online here](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/023_EDA_model_data.ipynb).

**PRELIMINARY CONCLUSIONS:**

These locational change by `crime-type` findings would suggest to us that, by including time-based predictors in our models [such as year-based property-related metrics such as those described in detail on our property assessment data EDA page](data-property.md), should increase the overall predictive accuracy of our models.

# Pair-wise relationship strength between predictors and `crime-type` classes

Looking beyond just location based and time-based predictors related to location, we will now examine the pair-wise relationships between our individual predictors versus each of our `crime-type` classes. To accomplish this, we will measure the strength of these relationships by calculating t-statistics for each of these pairings. Effectively, this will look in isolation at each predictor and class combination to determine the strength of that particular predictor's strength in predicting the that class outcome in a "one-vs-rest" fashion.

Outlined below are the top 6 predictors, as measured using t-statistic for each `crime-type` class:

```
The predictors with the largest t-statistics related
to each crime-type class are:

class 0: other

owner-occupied-ratio     22.273876
lat                      18.267198
poverty-rate             17.126022
median-age               17.011709
enrolled-college-perc    16.391080
streetlights-night        9.755394


class 1: burglary

commercial-mix-ratio            15.763925
night                           14.720921
lon                             13.690131
less-than-high-school-perc      10.112486
college-near                     9.622414
streetlights-night               9.404400


class 2: drugs-substances

night                         34.348157
streetlights-night            27.675943
industrial-mix-ratio          26.967262
Sunday                        25.628384
less-than-high-school-perc    23.495035
enrolled-college-perc         20.393787


class 3: fraud

less-than-high-school-perc           16.961052
Sunday                               16.769208
bachelor-degree-or-more-perc         14.736636
residential-median-value-3yr-cagr    14.617063
median-income                        11.651747
enrolled-college-perc                11.110884


class 4: harassment-disturbance

residential-gini-coef           64.197763
bachelor-degree-or-more-perc    64.109761
enrolled-college-perc           63.756338
commercial-mix-ratio            63.103933
residential-median-value        57.114483
college-near                    57.014002


class 5: robbery

less-than-high-school-perc           11.036563
streetlights-night                   10.144345
lon                                   8.767687
night                                 8.125654
bachelor-degree-or-more-perc          7.530712
residential-median-value-3yr-cagr     7.502349


class 6: theft

bachelor-degree-or-more-perc    68.596304
residential-gini-coef           61.648668
enrolled-college-perc           60.336105
residential-median-value        59.614084
less-than-high-school-perc      54.186831
college-near                    50.522663


class 7: vandalism-property

commercial-mix-ratio            26.472810
college-near                    22.720740
residential-median-value        21.418503
residential-gini-coef           20.612366
enrolled-college-perc           19.228918
owner-occupied-ratio            12.646433


class 8: violence-aggression

less-than-high-school-perc      20.034071
bachelor-degree-or-more-perc    17.884468
median-income                   15.808026
streetlights-night              15.316972
residential-gini-coef           15.112320
poverty-rate                    14.026041
```

Now, for the sake of consistency with the previous section of this EDA, we will use plots to examine these top 5 predictors for the sames subset of predictors `burglary`, `drugs-substances`, and `harassment-disturbance`.

![tstat-burg]({{ site.url }}/figures/features/tstat-top-pred-burglary.png)

![tstat-drug]({{ site.url }}/figures/features/tstat-top-pred-drugs-substances.png)

![tstat-harass]({{ site.url }}/figures/features/tstat-top-pred-harassment-disturbance.png)

**PRELIMINARY CONCLUSIONS:**

In above summary tables and plots, we can see a fairly broad mixture of top 5 predictors across all of our `crime-type` classes. This leads us to believe that we may have a suitable variety of predictors for the classes we hope to predict. However, while some `crime-type` classes such as `theft` and `harassment-disturbance` have top predictors with t-statistics exceeding 60, some classes such as `violence-aggression`, `robbery`, and `burglary` have much smaller top t-statistic values less than 25. This suggests those classes may be prove to be harder to predict accurately using this set of predictors. However, what's not accounted for in these t-statistic measures is the potential interaction effect of trying to generate predictions for each specific `crime-type` class with multiple predictors at once.

# Evaluating distance-based geographical predictors by class

In the previous section of this EDA, we saw a couple of our distance-based predictors in the top 5 predictors for several of the `crime-type` classes. This leads us to wonder how these predictors might vary overall among all of our class types. The specific predictors we would consider distance-based are `streetlights-night`, which measures the number of streetlights within 100 meters of each crime record for crimes occuring at night, `college-near`, which indicates whether or not a crime incident occured wihtin 500 meters of a college or university, and `highschool-near`, which indicates whether a crime incident occured within 500 meters of a public or non-public highschool.

All measurements used in these predictors were calculated using the Haversine formula to measure the distance between sets of latitude and longitude coordinates. [A detailed description of the Haversine implementation built for our analysis can be found on this site page](haversine.md).

Below we can 