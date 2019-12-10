---
title: "City of Boston Crime Indcidents EDA"
---

# Source materials

Here is a list with links to the jupyter notebook and original dataset used to generate the findings on this page:

- [The EDA notebook used to generate the below findings can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/009_EDA_crime_incident_reports.ipynb) 

- [The original City of Boston crime incident reports data for all years analyzed can be found online here.](https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system)

# Summary and challenges

The City of Boston’s crime incident reports (August 2015 - to date) data is the source data for the parameter of interest in our analysis, "crime type". [The original dataset managed by the City of Boston](https://data.boston.gov/dataset/crime-incident-reports-august-2015-to-date-source-new-system) contained 436,666 crime incident observations, spanning 66 different crime “offense code groups” across the City of Boston.

![records-by-year]({{ site.url }}/figures/crime/crime-reports-by-year.png)

Due to limitations imposed by years of available property assessment data (for details concerning the property assessment data used in this analysis, [please see this page](data-property.md)), and the limited number of 2015 observations, we decided to use incident reports for just the 2016-2019 calendar years. Because of the geospatial nature of our analysis, we also excluded 35,785 additional records with missing latitude and longitude coordinates. And, due to a disproportionately large proportion of records during the final 3 months of observations (Sep.-Nov 2019) with missing coordinate data, those three months were excluded as well. By subsetting our data to Jan. 2016 through Aug. 2019, and excluding observations with missing coordinates, we were left with 347,284 crime incident observations from which to work.

# Consilidating "crime type" classes

Because we are dealing with a classification challenge, we also felt it was important to consolidate our 66 offense code groups into a smaller subset of “crime types” to generate more meaningful results later in our analysis. To accomplish this, we (a) removed incident categories of little interest that might otherwise obscure trends in more important areas of crime (for instance ambiguous categories like “investigations” or non-crime categories like “motor vehicle accident response”) and (b) consolidated the remaining categories into a set of 9 different “crime types”: burglary, drugs-substances, fraud, harassment-disturbance, robbery, theft, vandalism-property, violence-aggression, and other. Once we dropped unused offense codes and were able to tie each record to its corresponding census tract shape (the geospatial unit of analysis used to summarize our property-related features), we were left with 151,072 records for our analysis, distributed as shown below: 


By referring to our accompanying notebook, you can also view additional EDA steps such as our investigation of potential observation bias in the observations with missing location coordinates.