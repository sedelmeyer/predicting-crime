---
title: "City of Boston Streetlights Data EDA"
---

## Source materials 

Here is a list with links to the jupyter notebook and original dataset used to generate the findings on this page:

- [The streelights notebook can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/017_EDA_street_lights.ipynb)
- [The original City of Boston street light data can be found online here.](https://data.boston.gov/dataset/streetlight-locations)

There are **74,065** streetlights listed by their lat and long in this dataset. All records are of type LIGHT so the only useful information in this dataset is the location of the light.   Given this we first plotted out each of the lights on a map of the city of Boston. The map shows a sparse distribution of light locations in the lower-left corner of the map. 

![street-lights_overall]({{ site.url }}/figures/streetlights/street-lights_overall.png)

## Missing Data
This is shown more clearly by comparing two figures below. The bottom figure indicates that there are multiple streets with no lights in zip code 02132 (West Roxbury). 

![street-lights_dense]({{ site.url }}/figures/streetlights/street-lights_dense.png)

![street-lights_missing]({{ site.url }}/figures/streetlights/street-lights_missing.png)

To explore whether this sparsity was in fact missing data, we investigated Google Street View to explore some of these West Roxbury streets. We found that these streets do indeed have streetlights *(as is shown in the photograph below)* confirming that this dataset is not a complete representation of streetlights in Boston.  This missing streetlight data has the potential of skewing any model that uses this information as a predictor.

![street-lights_street-view]({{ site.url }}/figures/streetlights/street-lights_present-01.png)

## Feature Engineering
However, to further explore the usefulness of this data and any effect of this missing data, we have begun work on engineering a model feature that measures streetlight density within 100 meters (configurable) of each crime in the crime dataset. For example, here are the number of streetlights within 100 meter proximity of the first twenty observations in the crime dataset:

``[0, 4, 8, 55, 43, 37, 53, 33, 33, 27, 28, 54, 54, 28, 33, 2, 26, 19, 22, 31]. ``
