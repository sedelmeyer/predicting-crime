---
title: "City of Boston Liquor License Data EDA"
---

[The liquor data prep notebook can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/012_liquor_data_prep.ipynb)

[The liquor data EDA notebook can be found here.](https://github.com/sedelmeyer/predicting-crime/blob/master/notebooks/013_EDA_liquor_data.ipynb)

Examining liquor licenses in Boston took a fair amount of data cleansing efforts to transform incomplete addresses to latitude and longitude. We have successfully processed **over 1,100 liquor license records** and plotted them in the figure below:

![liquor-license-map]({{ site.url }}/figures/liquor/liquorLicenses.png)

> What we’ve found a bit peculiar is that several of our data points fall outside our map. 

## Liquor License Categories

Digging a bit deeper we’ve found that **over 85%** of our liquor license categories belong to **"Common Victualler"** which represents "any establishment that has on its premises the ability to assemble, prepare, or cook food". 

> We would not expect such an unequal distribution of liquor license types which raises concern towards the completeness of our dataset. Given these concerns we may decide to exclude the presence of liquor licenses in our final model.

![liquor-license-categories]({{ site.url }}/figures/liquor/liquorLicenseCategories.png)

![liquor-license-categories-simplified]({{ site.url }}/figures/liquor/liquorLicenseCatSimplified.png)
