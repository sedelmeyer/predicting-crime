---
title: "Modeling using Decision Trees"
---

[The Decision Tree notebook can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/031_MODEL_decision_trees.ipynb)


## Model tuning


**Model 1** 

![trees_dif_depths]({{ site.url }}/figures/model-trees/trees_dif_depths.png)

**Model 2** 


**Model 3** was run with 



## Model results
We then took our best 



## Predictors *(included here for reference)*

Listed below are the predictors used in our KNN model:
*(Additional predictors still under development for future iterations of our model are listed separately in Appendix 1 of this document.)*

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