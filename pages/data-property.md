---
title: "City of Boston Property Assessment Data EDA"
---

A copy of the EDA notebook used to generate the below findings can be found here:

[https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/010_EDA_boston_property_assessments.ipynb](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/010_EDA_boston_property_assessments.ipynb) 

The City of Boston’s property assessment records provided data we used to engineer several features for our baseline model. The records used for our analysis can be found on the Boston Analyze website and included all Boston properties, by Parcel ID (PID) and address, from fiscal years 2013 to 2019. This consolidated dataset included 1,185,432 total property assessment records and the largest challenge associated with this data was matching location coordinates to years of data with no recorded location coordinates (approx. 1,083,590 records). By matching PIDs for years with reporting coordinates, the vast majority of these missing coordinates were matched. For the remaining 78,018 unmatched records, the City of Boston’s Live Street Address Management (SAM) System parcel dataset was used for matching. With the SAM dataset, we were able to match coordinates to all but 32,297 assessment records for a 98.5% total match rate (see plot below).

![property-location-match]({{ site.url }}/figures/property/match-FINAL.png)

With these matched coordinates, we were able to explore the dataset for features of interest that we could aggregate within geospatial regions. From this, we engineered a set of 10 property-based predictors, each providing a census tract-level metric per-year to give (1) a point in time measure for that geographic area, as well as (2) a 3-year average annual change rate to measure shifting property demographics for the area. The full set of features are described below in the “Baseline Model” section of this report (listed as predictors 4 through 13). Here are two plots illustrating a sample of these engineered features:

![property-median-gini]({{ site.url }}/figures/property/property-residential-median-gini-by-census%20tract.png)

![property-median-gini-3yr]({{ site.url }}/figures/property/property-residential-median-gini-CAGR-by-census%20tract.png)
