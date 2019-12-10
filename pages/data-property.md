---
title: "City of Boston Property Assessment Data EDA"
---

# Source materials

Here is a list with links to the jupyter notebook and original datasets used to generate the findings on this page:

- [The EDA notebook used to generate the below findings can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/010_EDA_boston_property_assessments.ipynb) 

- [The original City of Boston property assessment data for all years analyzed can be found online here.](https://data.boston.gov/dataset/property-assessment)

- [The City of Boston's Live Street Address Management (SAM) System property property parcel dataset can be found online here.](https://data.boston.gov/dataset/live-street-address-management-sam-addresses)

# Summary and challenges

The City of Boston’s property assessment records provided data we used to engineer several features for our baseline model. The records used for our analysis [can be found here](https://data.boston.gov/dataset/property-assessment) on the Boston Analyze website and included all Boston properties, by Parcel ID (PID) and address, from fiscal years 2013 to 2019. Once consolidated for all these years, the dataset included 1,185,432 total property assessment records as well as 80 different features with which each property was characterized. The largest challenges associated with this data was matching location coordinates to years of data with no recorded location coordinates (approx. 1,083,590 records), as well as identifying which of the 80 features were meaningful enough with minimal missing data for the creation of engineered features for use in our resulting crime prediction model.

# Matching coordinates to records

By matching Parcel IDs (PIDs) for the subset of years with already reported coordinates (only some years included coordinates by default), the vast majority of these missing coordinates were matched. For the remaining 78,018 unmatched records, we turned to the City of Boston’s Live Street Address Management (SAM) System parcel dataset, which [can be found here](https://data.boston.gov/dataset/live-street-address-management-sam-addresses). With the SAM dataset, we were able to match coordinates to all but 32,297 assessment records for a 98.5% total match rate (see plot below). While the plot below indicates that there are still pockets of unmatched SAM property parcels (as indicated by the visible orange points below), the remaining 1.5% unmatched property assessment records lack specific street addresses or any other features which will make matching of those records feasible. While a future iteration of this analysis may provide sufficient time to explore methods for imputing this missing data, it is outside the scope of the current analysis.  

![property-location-match]({{ site.url }}/figures/property/match-FINAL.png)

# Feature engineering

With these matched coordinates, we were able to explore the dataset for features of interest that we could aggregate within geospatial regions. From this, we engineered a set of 10 property-based predictors, each providing a census tract-level metric per-year to give (1) a point-in-time annual measure for that tract-level geographic area, as well as (2) a 3-year compound annual growth rate (CAGR) to measure shifting property demographics for the area.

The full set of census tract-level engineered features derived from the property assessment dataset are:

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


described below in the “Baseline Model” section of this report (listed as predictors 4 through 13). Here are two plots illustrating a sample of these engineered features:

![property-median-gini]({{ site.url }}/figures/property/property-residential-median-gini-by-census%20tract.png)

![property-median-gini-3yr]({{ site.url }}/figures/property/property-residential-median-gini-CAGR-by-census%20tract.png)
